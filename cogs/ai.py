import os
from groq import Groq
from discord.ext import commands

client_ai = Groq(api_key=os.getenv("GROQ_API_KEY"))


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, *, pergunta: str):
        async with ctx.typing():
            try:
                resposta = client_ai.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Responda de forma curta e direta, sem enrolação. Evite listas longas e textos extensos."},
                        {"role": "user", "content": pergunta}
                    ]
                )
                texto = resposta.choices[0].message.content
                for i in range(0, len(texto), 2000):
                    await ctx.send(texto[i:i+2000])
            except Exception as e:
                await ctx.send(f"Erro: {e}")


async def setup(bot):
    await bot.add_cog(AI(bot))
