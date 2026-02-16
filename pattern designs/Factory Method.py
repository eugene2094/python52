class MorningGreeting:
    def greet(self):
        print("Good morning !")


class AfternoonGreeting:
    def greet(self):
        print("Good afternoon !")


class EveningGreeting:
    def greet(self):
        print("Good evening !")


class GreetingFactory:
    def creating_greeting(self, time):
        if time == 'morning':
            return MorningGreeting()
        elif time == 'afternoon':
            return AfternoonGreeting()
        elif time == 'evening':
            return EveningGreeting()


greeting_factory = GreetingFactory()
morning = greeting_factory.creating_greeting("morning")

morning.greet()
evening = greeting_factory.creating_greeting("evening")
evening.greet()
