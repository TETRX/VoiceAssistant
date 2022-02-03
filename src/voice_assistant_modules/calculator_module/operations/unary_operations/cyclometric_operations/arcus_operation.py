from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation


class ArcusOperation(UnaryOperation):
    @classmethod
    def get_keywords(cls):
        keywords = super(ArcusOperation, cls).get_keywords()
        keywords = keywords + \
               tuple(word.replace("arcus", "arkusz") for word in keywords)  # speech_recognition likes hearing "arkusz"
        # instead of "arcus" in more complicated queries.
        return keywords