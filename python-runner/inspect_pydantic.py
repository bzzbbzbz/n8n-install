
try:
    from pydantic_ai.models.openai import OpenAIModel
    import inspect
    print("OpenAIModel found")
    print(inspect.signature(OpenAIModel.__init__))
except Exception as e:
    print(e)

