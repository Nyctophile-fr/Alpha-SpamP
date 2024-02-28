import discord
from discord.ext import commands
import colorama
from colorama import Fore
from discord.ui import View, Button
import asyncio
from typing import Optional
import json

bot_tokens = ['OTk3NDc3MjUxMDczNDYyMzUz.GG0avf.2y4B8jf-JKcb3ILLhjGCCvvq2u10SC37iX_3KQ', 'MTAxODQ3MTUwMzE5NDQ4ODg1Mg.GApwu8.UFE3XdLWAETXbXsFEm7LpMCRJzygDeI8lfb1L0', 'MTAzNTExMzE0NDkyNzkzMjQ5Ng.GAiVCn.4T2jvSmyJ7N6E_RJSUPY8oKkXT4-iQzBKVCWew', 'MTE5ODY1Nzc4MDUzMDI5NDgzNg.GWN-OW.O7U5klx83yLyRY2sdioRHT5AX45HXUhBZFpVAE', 'MTE5ODY1NzkwOTMxNjM5NTAzOA.G455xc.OPCQIHeEVbeNybW_Mjky8FR8aZWjZVGI8d64tw', 'MTE5ODY1ODA1NTA2MDA3ODYwMg.GROt9u.kwWHuFkrlAi8FdN7tylTBX7Qpr4VwX7SyPMFss', 'MTE5ODY1ODI5NzY4Nzk2NTcxNg.GZXZZt.cXU63iRgKNnRv61GbE426gwvM4Fv6wMyhIJgh4', 'MTE5ODY1ODQ3MDI0MTY0NDU5NA.GrYd4L.fTvFVGFqbf6_hXXpsDsKiYen7swnrFVncJO4Ic', 'MTE5ODY1ODU5OTc1NzU2MTg2Ng.GNB-IT.UY3sCl-gj93IXJmCxg8pQHdcy0lf8hzguBqGsA', 'MTE5ODk5Mzk1MjY5NTY2MDU5NA.GKAt9B.y9M_JUndQSv5VtTAdudMVJAVHS1nYGeHJdIwlc', 'MTE5ODk5NzIxMDc0MjkxOTI1MA.Gq32bS.JFaghFolYHQSVSiXGWqHKSh9Ct5Fa3aDcVTM08']
bots = []

json_file_path = 'secured_users.json'

class Lemon(discord.ui.View):
  def __init__(self, ctx: commands.Context, timeout: Optional[int] = None):
      super().__init__(timeout=timeout)
      self.ctx = ctx

  async def interaction_check(self, interaction: discord.Interaction):
      if interaction.user.id != self.ctx.author.id:
          await interaction.response.send_message("You can't use this command", ephemeral=True)
          return False
      elif interaction.user.id == "889005501701029919":
          return False
      return True


class PingView(Lemon):
  def __init__(self, ctx: commands.Context):
      super().__init__(ctx, timeout=None)
      self.value = None

  @discord.ui.button(label="Check Latency", custom_id="Ping", style=discord.ButtonStyle.grey)
  async def pingg(self, interaction, button):
      self.value = "Ping"
      self.stop()


class MyCog(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      self.correct = 0x00ff0b
      self.wrong = 0xe61111
      self.color = 0x2f3136

  @commands.command(name='ping')
  async def ping(self, ctx):
      latency = round(self.bot.latency * 1000)
      pong = f"🏓Ping: **{latency}ms**"
      if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
          await ctx.send(content=pong)
      else:
          print(Fore.RED + "Skipped Ping Command By Me")


  @commands.command(name='spam')
  async def spam(self, ctx, user: discord.User, *, message):
      if not message:
          if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
              await ctx.reply(embed=discord.Embed(description="<:crosss:1190988421762650192> | Error: Please provide a message.", color=0xe61111))
          else:
              print(Fore.RED + "Error user not gaved msg spam command skipped by me")
              return

      # Get the user mentioned in the command
      target_user = self.bot.get_user(user.id)

      # Check if the target user exists
      if target_user:
          # Check if the target user is in the secured set
          if target_user.id in secured_users:
              if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
                  await ctx.reply(embed=discord.Embed(description="<:crosss:1190988421762650192> | You can't mention a **secured** user.", color=0xe61111))
              print(Fore.RED + "Skipped Spam Command By Me")
          else:
              # Construct the final message with the user's input and a fixed link
              final_message = f"{ctx.author.mention} Spammed You: {message}\n> Join https://discord.gg/HAbFwJHJsg"

              # Send the message to the target user three times
              for _ in range(3):
                  await target_user.send(final_message)

              if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
                  await ctx.reply(embed=discord.Embed(description=f"<:tickkk:1190988406709297192> | Succesfully sent the message to {target_user.mention}\nMessage: {final_message}", color=0x00ff0b))
              else:
                  print(Fore.RED + "Skipped Spam Command By Me")
      else:
          if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
              await ctx.reply(embed=discord.Embed(description="<:crosss:1190988421762650192> | Error: User not found.", color=0xe61111))
          else:
              print(Fore.RED + "User not found spam skipped by me")

  @commands.command(name='secure')
  async def secure(self, ctx):
      # Add the user ID to the secured set
      secured_users.add(ctx.author.id)
      if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
          await ctx.reply(embed=discord.Embed(description=f"<:tickkk:1190988406709297192> | {ctx.author.mention} has been **secured**.", color=0x00ff0b))
          # Save the updated secured users to the JSON file
          save_secured_users()
      else:
          print(Fore.RED + "Skipped secure command by me")




  @commands.command()
  async def secure_add(self, ctx, *, user: discord.Member):
      # Add the user ID to the secured set
      secured_users.add(user.id)
      if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
          await ctx.reply(embed=discord.Embed(description=f"<:tickkk:1190988406709297192> | {user.mention} has been **secured**.", color=0x00ff0b))
          # Save the updated secured users to the JSON file
          save_secured_users()
      else:
          print(Fore.RED + "Skipped secure command by me")
  
  
      

  @commands.command(name='insecure')
  async def insecure(self, ctx):
      # Remove the user ID from the secured set
      secured_users.discard(ctx.author.id)
      if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
          await ctx.send(embed=discord.Embed(description=f"<:tickkk:1190988406709297192> | {ctx.author.mention} has been **insecured**.", color=0x00ff0b))
          # Save the updated secured users to the JSON file
          save_secured_users()
      else:
          print(Fore.RED + "Skipped insecure command by me")



  @commands.command()
  async def secure_remove(self, ctx, *, user: discord.Member):
      # Remove the user ID from the secured set
      secured_users.discard(user.id)
      if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
          await ctx.send(embed=discord.Embed(description=f"<:tickkk:1190988406709297192> | {user.mention} has been **insecured**.", color=0x00ff0b))
          # Save the updated secured users to the JSON file
          save_secured_users()
      else:
          print(Fore.RED + "Skipped insecure command by me")
  


  @commands.command(name='help')
  async def help(self, ctx):
      if any(role.id == 1198684416793378817 for role in ctx.guild.me.roles):
          embed = discord.Embed(
            title="**__COMMANDS LIST__**",
            description="""
```
$ping - (Check Bot Latency)
$secure - (Secure Yourself)
$insecure - (Unsecure Yourself)
$spam @user <message> - (Spam a user)
```         
""",
            color=self.color)
          embed.add_field(name="**__DEVELOPER COMMANDS__**",
                         value="""
```
$secure_add @user - (Unsecure a user)
$secure_remove @user - (Secure a user)
```                         
""",
                         inline=False)
          await ctx.send(embed=embed)
      else:
          print(Fore.RED + "Skipped help command by me")

# Function to load secured users from the JSON file
def load_secured_users():
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return set(data['secured_users'])
    except FileNotFoundError:
        return set()

# Function to save secured users to the JSON file
def save_secured_users():
    data = {'secured_users': list(secured_users)}
    with open(json_file_path, 'w') as file:
        json.dump(data, file)

# Load secured users on startup
secured_users = load_secured_users()


async def start_bots():
  async def on_ready():
      print(Fore.BLUE + f"{bot.user.name} is ready!")
      await bot.add_cog(MyCog(bot))
      await bot.load_extension("jishaku")
      print(Fore.MAGENTA + "Cog loaded")
      print(Fore.MAGENTA + "Jishaku loaded")
      print(Fore.YELLOW + "All Bots Are Ready Now!")

  for token in bot_tokens:
      bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
      bot.remove_command('help')
      owner_ids = [1020693089851027457]
      bot.owner_ids = owner_ids

      bot.add_listener(on_ready, 'on_ready')

      cog = MyCog(bot)
      await bot.add_cog(cog)

      bots.append(bot)

  await asyncio.gather(*[bot.start(token) for bot, token in zip(bots, bot_tokens)])
  print(Fore.BLUE + "All bots started.")


if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  try:
      loop.run_until_complete(start_bots())
      loop.run_forever()
  except KeyboardInterrupt:
      print("KeyboardInterrupt: Closing bots gracefully...")
      loop.run_until_complete(asyncio.gather(*[bot.close() for bot in bots]))
      loop.run_until_complete(loop.shutdown_asyncgens())
      loop.close()