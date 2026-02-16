class ConsoleLogManager:
    _instance = None

    def __init__(self):
        if ConsoleLogManager._instance is not None:
            raise Exception("Only one instance can create !")
        else:
            ConsoleLogManager._instance = self

    @staticmethod
    def getInstance():
        if ConsoleLogManager._instance is None:
            ConsoleLogManager()
        return ConsoleLogManager._instance

    def log(self, message):
        print(f"Log entry: {message}")


log_manager = ConsoleLogManager.getInstance()
log_manager.log("Singleton pattern is working !")

log_manager2 = ConsoleLogManager()
