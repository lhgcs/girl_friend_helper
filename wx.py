from wxpy import
bot = Bot()
all_group = bot.group()[0:]

for i in all_group:
    Group = str(i)
    group = Group.replace("<Group:"."").replace(">","")
    send_message = bot.group().search(group)[0].send_image("1.jpg")
