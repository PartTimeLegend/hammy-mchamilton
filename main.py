import asyncio
import discord
import random
import os

class QuizBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quiz_types = {
            "foundation": "foundation_quiz.txt",
            "intermediate": "intermediate_quiz.txt",
            "full": "full_quiz.txt"
        }

    async def on_ready(self):
        print('Bot is ready.')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!quiz'):
            await self.handle_quiz_request(message)

    async def handle_quiz_request(self, message):
        parts = message.content.split()
        if len(parts) < 2:
            await message.channel.send("Please specify a quiz type. Usage: !quiz <quiz_type>")
            return
        quiz_type = parts[1].lower()
        if quiz_type not in self.quiz_types:
            await message.channel.send("Quiz type not found.")
            return
        await self.ask_question(message, quiz_type)

    async def ask_question(self, message, quiz_type):
        questions_file = self.quiz_types[quiz_type]
        questions = self.read_questions(questions_file)
        if not questions:
            await message.channel.send("Error: Failed to load questions.")
            return
        question, answer = random.choice(list(questions.items()))
        await message.channel.send(question)
        response = await self.wait_for_response(message)
        await self.check_answer(message, response, answer)

    async def wait_for_response(self, message):
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel
        try:
            response = await self.wait_for('message', check=check, timeout=10.0)
            return response.content.lower()
        except asyncio.TimeoutError:
            await message.channel.send("Time's up! No response received.")
            return None

    async def check_answer(self, message, response, answer):
        if response is None:
            await message.channel.send("No response received. The correct answer was: {}".format(answer))
            return
        if response == answer.lower():
            await message.channel.send("Correct!")
        else:
            await message.channel.send("Incorrect! The correct answer was: {}".format(answer))

    def read_questions(self, file_path):
        questions = {}
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    question, answer = line.strip().split('|')
                    questions[question] = answer
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error reading file '{file_path}': {e}")
        return questions

# Run the bot with the Discord bot token read from an environment variable
intents = discord.Intents.default()
intents.message_content = True
bot = QuizBot(intents=intents)
bot.run(os.environ['DISCORD_BOT_TOKEN'])
