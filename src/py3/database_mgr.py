import sqlite3
import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


class DatabaseQABackend():
    """Class to handle the database connection and the sentence transformer model, as well as by fetching closest answer to a given question, please note, this class only handles user QA."""
    
    def __init__(self, db_path:str, sentence_transformer_path:str='sentence-transformers/all-MiniLM-L6-v2'):
        """Default constructor, initializes the database connection and the sentence transformer

        Args:
            db_path (str): path to QA sqlite database
            sentence_transformer_path (str): path to 'all-MiniLM-L6-v2' model
        """
        # conenct and prepare the database
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        # load model and tokenizer for calculating sentence embeddings
        self.tokenizer = AutoTokenizer.from_pretrained(sentence_transformer_path)
        self.model = AutoModel.from_pretrained(sentence_transformer_path)
        # load the sentence embeddings cacahe from database
        self.cursor.execute("SELECT answer_id, embedding FROM answer_embeddings")
        self.sentence_embedding_cache = self.cursor.fetchall()

    def get_answer(self, question:str, knn_answer_count:int=5) -> list:
        """Get the closest answers to a given question

        Args:
            question (str): User's question
            knn_answer_count (int, optional): top-k most relevant want to obtain. Defaults to 5.

        Returns:
            list: top-k answers
        """
        question_embedding = self._sentence_embedding(question)
        
        # list all the answers and their embeddings stored in the database
        question_list = [(question_id, embedding) for question_id, embedding in self.sentence_embedding_cache]
        # get sorted list of answers based on cosine similarity
        def distance(question_embedding, answer_embedding_object) -> float:
            db_embedding = np.frombuffer(answer_embedding_object[1], dtype=np.float32)
            question_embedding = question_embedding[0]
            return cosine_similarity([question_embedding], [db_embedding])[0][0]
        question_list.sort(key=lambda x: distance(question_embedding, x), reverse=True)
            
        # fetch the top knn_answer_count answers from database with given FK answer_id.
        answers = []
        for i in range(knn_answer_count):
            answer_id = question_list[i][0]
            self.cursor.execute("SELECT answer_text FROM HistoricalQA WHERE id=?", (answer_id,))
            answers.append(self.cursor.fetchone()[0])
        # Return the output
        return answers
    
    def _sentence_embedding(self, sentence:str) -> np.ndarray:
        """function to get the sentence embedding of a given sentence, make devs able to use something like cosine similarity to compare the embeddings

        Args:
            sentence (str): sentence to get the embedding of
            
        Returns:
            ndarray: the sentence embedding
        """
        inputs = self.tokenizer(sentence, return_tensors="pt")
        model_out = self.model(**inputs)
        embeddings = model_out.last_hidden_state[:, 0, :]
        embeddings_np = embeddings.detach().numpy()
        return embeddings_np
    
    def __del__(self):
        """ Destructor, closes the database connection """
        self.conn.close()