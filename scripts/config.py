import os
import openai
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


class Singleton(type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):
        self.continuous_mode = False
        self.speak_mode = False
        # TODO - make these models be self-contained, using langchain, so we can configure them once and call it good 
        self.fast_llm_model = os.getenv("FAST_LLM_MODEL", "gpt-3.5-turbo") 
        self.smart_llm_model = os.getenv("SMART_LLM_MODEL", "gpt-4")
        self.fast_token_limit = int(os.getenv("FAST_TOKEN_LIMIT", 4000))
        self.smart_token_limit = int(os.getenv("SMART_TOKEN_LIMIT", 8000))
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.use_azure = False
        self.use_azure = os.getenv("USE_AZURE") == 'True'
        if self.use_azure:
            self.openai_api_base = os.getenv("OPENAI_API_BASE")
            self.openai_api_version = os.getenv("OPENAI_API_VERSION")
            self.openai_deployment_id = os.getenv("OPENAI_DEPLOYMENT_ID")
            openai.api_type = "azure"
            openai.api_base = self.openai_api_base
            openai.api_version = self.openai_api_version
        
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.custom_search_engine_id = os.getenv("CUSTOM_SEARCH_ENGINE_ID")

        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_region = os.getenv("PINECONE_ENV")

        # User agent headers to use when browsing web
        # Some websites might just completely deny request with an error code if no user agent was found.
        self.user_agent_header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        # Initialize the OpenAI API client
        openai.api_key = self.openai_api_key

    def set_continuous_mode(self, value: bool):
        self.continuous_mode = value

    def set_speak_mode(self, value: bool):
        self.speak_mode = value

    def set_fast_llm_model(self, value: str):
        self.fast_llm_model = value

    def set_smart_llm_model(self, value: str):
        self.smart_llm_model = value

    def set_fast_token_limit(self, value: int):
        self.fast_token_limit = value

    def set_smart_token_limit(self, value: int):
        self.smart_token_limit = value

    def set_openai_api_key(self, value: str):
        self.openai_api_key = value
    
    def set_elevenlabs_api_key(self, value: str):
        self.elevenlabs_api_key = value
        
    def set_google_api_key(self, value: str):
        self.google_api_key = value
    
    def set_custom_search_engine_id(self, value: str):
        self.custom_search_engine_id = value

    def set_pinecone_api_key(self, value: str):
        self.pinecone_api_key = value

    def set_pinecone_region(self, value: str):
        self.pinecone_region = value