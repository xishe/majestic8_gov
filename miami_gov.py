import disnake
from disnake.ext import commands
from disnake import TextInputStyle, Button, ui
from typing import Optional
import datetime
import collections
import asyncio
import json
import disnake
from disnake.ext import commands
from disnake import Embed
import json
import datetime

bot = commands.Bot(command_prefix=".", intents=disnake.Intents.all())


@bot.event
async def on_member_join(member):
    # ID канала, куда нужно отправить сообщение
    channel_id = 1119326879564972148  
    channel = bot.get_channel(channel_id)
    if channel is not None:
        embed = disnake.Embed(
            title="Добро пожаловать во фракцию Goverment",
            description="Перед началом работы, тебе нужно изменить никнейм на сервере по этой форме:\n\n"
                        "Отдел | Имя Фамилия | Static ID (для USSS)\n"
                        "Должность | Имя Фамилия | Static ID (для всех остальных)\n\n"
                        "Пример:\n"
                        "ECTF | Rick Immortal | 43642\n"
                        "Адвокат | Rick Immortal | 43642",
            color=0x2F3136,
            timestamp=datetime.datetime.now()
        )
        embed.set_thumbnail(url='https://i1.imageban.ru/out/2024/04/29/29a3ec96ab4bea5d22fb3718b991454a.png')
        embed.set_footer(text=f"ID пользователя: {member.id}")
        await channel.send(f'{member.mention}', embed=embed)


@bot.command()
async def staff_fsd(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Head of FSD': [1161056980941684747],
        'Deputy Head of FSD': [1161058031774216334],
        'FSD USSS': [1161048435730956338],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав FSD", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_mk(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Министр Культуры': [1119924452965240832],
        'Заместители Министра Культуры': [1119924778434834472],
        'Менеджеры культуры': [1149708866179825845],
        'Стажеры культуры': [1144453558335459328],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав Министерства Культуры", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_mz(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Министр Здравоохранения': [1119326877807554688],
        'Заместители Министра Здравоохранения': [1119326877794975925],
        'Менеджеры здравоохранения': [1119634461198405753],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав Министерства Здравоохранения", timestamp=datetime.datetime.now(),
                              color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_ectf(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Head of ECTF': [1223205925037543464],
        'Deputy Head ECTF': [1223206228998623232],
        'ECTF USSS': [1223205550783987813],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав ECTF", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_usss(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Министр Безопасности': [1119326877820133501],
        'Заместители Министра Безопасности': [1119326877807554680],
        'Директор USSS': [1119326877820133497],
        'Заместители Директора USSS': [1119326877774000144],
        'ECTF': [1223205925037543464, 1223206228998623232],
        'RTPD': [1119326877774000141, 1122206265284767765],
        'ECHO': [1139529463437213746, 1139530097280421918],
        'FSD': [1161056980941684747, 1161058031774216334],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав United States Secret Service", timestamp=datetime.datetime.now(),
                              color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_ld(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Министр Финансов': [1119326877807554689],
        'Заместители Министра Финансов': [1119326877794975922],
        'Директор LD': [1139165924826562660],
        'Заместители Директора LD': [1139166159887937539],
        'Лицензеры': [1119945876589264916],
        'Стажеры LD': [1193944327483834538],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав Лицензеров", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_advokat(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Глава Коллегии Адвокатов': [1119326877807554683],
        'Заместители Главы Коллегии Адвокатов': [1120369701411889152],
        'Адвокаты': [1119326877740441673],
        'Юристы': [1119326877740441672],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав Адвокатуры", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_sud(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Председатель Верховного Суда': [1119326877820133502],
        'Верховные судья': [1119326877757227065],
        'Председатель Окружного Суда': [1121421400540975134],
        'Окружные Судья': [1119326877757227063],
        'Судебные секретари': [1126805044705108049],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав Судей", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def staff_rtpd(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Head RTPD': [1119326877774000141],
        'Deputy Head RTPD': [1122206265284767765],
        'RTPD USSS': [1120813079299620946],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Состав RTPD", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


@bot.command()
async def high_staff(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Губернатор': [1119326877820133504],
        'Вице-Губернатор': [1119326877820133503],
        'Министерство Юстиции': [1119326877820133500, 1119326877794975924],
        'Министерство Безопасности': [1119326877820133501, 1119326877807554680],
        'Министерство Финансов': [1119326877807554689, 1119326877794975922],
        'Министерство Обороны': [1138884817228935311, 1138885355983085679],
        'Министерство Здравоохранения': [1119326877807554688, 1119326877794975925],
        'Министерство Культуры': [1119924452965240832, 1119924778434834472],
        'Судебная власть': [1119326877820133502, 1119326877757227065, 1121421400540975134, 1119326877757227063],
        'Адвокатура': [1119326877807554683, 1120369701411889152],
        'Отдел лицензирования': [1139165924826562660, 1139166159887937539],
        'USSS': [1119326877820133497, 1119326877774000144, 1119326877774000141, 1122206265284767765,
                 1139529463437213746, 1139530097280421918, 1151792701155586119, 1151793241721679903,
                 1151816937555382362, 1151817501445988373, 1161056980941684747, 1161058031774216334],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    def construct_embed():
        embed = disnake.Embed(title="Старший состав", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')

        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)
        return embed

    message = await ctx.send(embed=construct_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=construct_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


def load_prosecutors():
    try:
        with open("prosecutors.json", "r") as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return {
                    "San Andreas National Guard": [],
                    "Federal Investigation Bureau": [],
                    "Emergency Medical Services": [],
                    "Los Santos Police Department": [],
                    "Los Santos Sheriff County Department": []
                }
    except FileNotFoundError:
        return {
            "San Andreas National Guard": [],
            "Federal Investigation Bureau": [],
            "Emergency Medical Services": [],
            "Los Santos Police Department": [],
            "Los Santos Sheriff County Department": []
        }
    except json.JSONDecodeError:
        print("Error decoding JSON. File might be corrupted.")
        return {
            "San Andreas National Guard": [],
            "Federal Investigation Bureau": [],
            "Emergency Medical Services": [],
            "Los Santos Police Department": [],
            "Los Santos Sheriff County Department": []
        }


# Save prosecutors' lists to file
def save_prosecutors(prosecutors_data):
    with open("prosecutors.json", "w") as file:
        json.dump(prosecutors_data, file, indent=4)


# Function for autocompletion of list names
async def autocomp_lists(inter: disnake.ApplicationCommandInteraction, user_input: str):
    return [list_name for list_name in prosecutors.keys() if user_input.lower() in list_name.lower()]


# Command for adding a user to a list of prosecutors
@bot.slash_command(description="Добавить курирующего прокурора")
async def add_prosecutor(inter: disnake.ApplicationCommandInteraction, user: disnake.Member,
                         list_name: str = commands.Param(autocomplete=autocomp_lists)):
    if list_name in prosecutors:
        prosecutors[list_name].append(user.id)
        save_prosecutors(prosecutors)  # Save changes to file
        await inter.response.send_message(f"Пользователь {user.mention} добавлен в список {list_name}.", ephemeral=True)
    else:
        await inter.response.send_message("Неверное название списка.", ephemeral=True)


@bot.slash_command(description="Список курирующих прокуроров")
async def list_prosecutor(inter: disnake.ApplicationCommandInteraction,
                          list_name: str = commands.Param(autocomplete=autocomp_lists)):
    if list_name in prosecutors:
        if prosecutors[list_name]:
            embed = disnake.Embed(
                title=f"Список пользователей в {list_name}",
                description='\n'.join(f"<@{user_id}>" for user_id in prosecutors[list_name]),
                color=0x00ff00  # Green color
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            await inter.response.send_message(f"Список {list_name} пуст.", ephemeral=True)
    else:
        await inter.response.send_message("Неверное название списка.", ephemeral=True)


# Command for removing a user from a list of prosecutors
@bot.slash_command(description="Удалить курирующего прокурора")
async def remove_prosecutor(inter: disnake.ApplicationCommandInteraction, user: disnake.Member,
                            list_name: str = commands.Param(autocomplete=autocomp_lists)):
    if list_name in prosecutors:
        if user.id in prosecutors[list_name]:
            prosecutors[list_name].remove(user.id)
            save_prosecutors(prosecutors)  # Save changes to file
            await inter.response.send_message(f"Пользователь {user.mention} удален из списка {list_name}.",
                                              ephemeral=True)
        else:
            await inter.response.send_message(f"Пользователь {user.mention} не найден в списке {list_name}.",
                                              ephemeral=True)
    else:
        await inter.response.send_message("Неверное название списка.", ephemeral=True)


@bot.command()
async def staff_proc(ctx):
    await ctx.message.delete()  # Удалить сообщение с вызовом команды

    role_groups = {
        'Генеральный прокурор': [1119326877820133500],
        'Зам. Генерального Прокурора': [1119326877794975924],
        'Старший Прокурор': [1124700387513991279],
        'Прокурор': [1119326877740441676],
        'Помощник прокурора': [1119326877740441675],
    }

    server_id = 1119326877690110023
    guild = bot.get_guild(server_id)

    async def construct_and_send_embed():
        embed = disnake.Embed(title="Состав Прокуратуры", timestamp=datetime.datetime.now(), color=0x2F3136)
        embed.set_thumbnail(url=f'{ctx.guild.icon.url}')
        embed.set_footer(text="Актуально на", icon_url=f'{ctx.guild.icon.url}')
        users_ids = [member.id for member in guild.members]
        members_by_role_group = []
        checked_members = set()
        for group, roles in role_groups.items():
            group_members = []
            for min_role in roles:
                for i in range(len(users_ids)):
                    if users_ids[i] not in checked_members:
                        for mem_role in reversed(guild.get_member(users_ids[i]).roles):
                            if min_role == mem_role.id and users_ids[i] not in checked_members:
                                group_members.append(f"{mem_role.name} - {guild.get_member(users_ids[i]).mention}")
                                checked_members.add(users_ids[i])
                                break
            members_by_role_group.append((group, group_members))

        for group, members in members_by_role_group:
            if members:
                embed.add_field(name=group, value='\n'.join(members), inline=False)

        # Read prosecutors data
        with open('prosecutors.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        additional_members = []
        for department, members in data.items():
            for member_id in members:
                member_name = guild.get_member(member_id)
                if member_name:
                    additional_members.append(f"{department} - {member_name.mention}")
                else:
                    additional_members.append(f"{department} - <@{member_id}>")
        if additional_members:
            embed.add_field(name='Курирующие прокуроры', value='\n'.join(additional_members), inline=False)
        return embed

    message = await ctx.send(embed=await construct_and_send_embed())
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание перед каждым обновлением
            try:
                await message.edit(embed=await construct_and_send_embed())
            except disnake.NotFound:
                break  # Прервать цикл, если сообщение было удалено
    except asyncio.CancelledError:
        pass  # Просто выходим из цикла, если задача отменена

    try:
        await message.delete()
    except disnake.NotFound:
        pass  # Игнорировать ошибку, если сообщение уже удалено


# Load prosecutors' lists
prosecutors = load_prosecutors()


class EmbedSender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="say",
        description="Отправляет настраиваемое embed сообщение в канал."
    )
    async def say(self, inter: disnake.ApplicationCommandInteraction,
                  content: str = commands.Param(default="", description="Текст перед embed сообщением."),
                  embed_json: str = commands.Param(
                      name='embed_json',
                      description="Создайте embed_json на сайте: https://oldeb.nadeko.bot/"
                  )):
        await inter.response.defer(ephemeral=True)  # Откладываем ответ

        try:
            data = json.loads(embed_json)

            embed = Embed(
                title=data.get("title", "Без заголовка"),
                description=data.get("description", ""),
                color=disnake.Color(data.get("color", 0)),
                timestamp=datetime.datetime.now()
            )

            author_info = data.get("author")
            if author_info:
                embed.set_author(name=author_info.get("name", ""), icon_url=author_info.get("icon_url", ""))

            footer_info = data.get("footer")
            if footer_info:
                embed.set_footer(text=footer_info.get("text", ""), icon_url=footer_info.get("icon_url", ""))
            elif inter.author.avatar:
                embed.set_footer(text=f"{inter.author.display_name}", icon_url=inter.author.avatar.url)

            thumbnail_url = data.get("thumbnail")
            if thumbnail_url:
                embed.set_thumbnail(url=thumbnail_url)

            image_url = data.get("image")
            if image_url:
                embed.set_image(url=image_url)

            for field in data.get("fields", []):
                embed.add_field(name=field.get("name", "Без названия"), value=field.get("value", ""),
                                inline=field.get("inline", False))

            if content or data.get("plainText", "") or embed.fields or embed.title or embed.description:
                await inter.channel.send(content=content, embed=embed)
                await inter.edit_original_response(content="✔ Сообщение успешно отправлено.", embed=None)
            else:
                await inter.edit_original_response(content="❌ Сообщение не может быть пустым.", embed=None)

        except json.JSONDecodeError:
            await inter.followup.send("❌ Ошибка: Введенные данные не являются валидным JSON.", ephemeral=True)
        except Exception as e:
            await inter.followup.send(f"❌ Непредвиденная ошибка: {str(e)}", ephemeral=True)


bot.add_cog(EmbedSender(bot))


class ButtonView(disnake.ui.View):

    def __init__(self):
        super().__init__()

        self.add_item(disnake.ui.Button(style=disnake.ButtonStyle.secondary, label='Заяление на увольнение',
                                        custom_id='uval_button'))


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id == "uval_button":
        await inter.response.send_modal(modal=MyModal())


@bot.command()
async def plz(ctx):
    await ctx.send('sdadadsad', view=ButtonView())


@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов к работе!")


class MyModal(disnake.ui.Modal):
    def __init__(self):
        # Детали модального окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Имя Фамилия | ID-карта",
                placeholder="Rick Immortal | 43642",
                custom_id="Имя Фамилия | ID-карта",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="В каком министерстве вы находитесь:",
                placeholder="USSS",
                custom_id="В каком министерстве вы находитесь:",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Ваша должность | Ранг (Отдел для USSS)",
                placeholder="Агент USSS | 6 | CAT",
                custom_id="Ваша должность | Ранг (Отдел для USSS)",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Причина увольнения",
                placeholder="ПСЖ",
                custom_id="Причина увольнения",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Скриншоты инвентаря (imgur/yapx)",
                placeholder="imgur/yapx",
                custom_id="Скриншоты инвентаря (imgur/yapx)",
                style=TextInputStyle.short,
            ),
        ]
        super().__init__(
            title="Заявление на увольнение",
            custom_id="uval_tag",
            components=components,
        )

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Заявление на увольнение", colour=disnake.Color.orange(),
                              timestamp=datetime.datetime.now())
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        embed.set_footer(
            text="by x1she",
            icon_url="https://cdn.discordapp.com/attachments/969288747059412993/1174123812300783732/KaCuSJIkm4DiSZSUp78Q7BTDceasYve2ZnXZ_W-IUxGVDaPX9b2eQKEeg93DFEzChMRMA-uuhM7-fVoIPes_mow.jpg?ex=65667303&is=6553fe03&hm=7f72a6a508f6b7375315684ea75ddeab97627f9afa46137c390b72e90e89536c&",
        )
        role_id = 1120281902851567676  # ID роли которая может уволить
        # Создаем вложение с модальным окном
        view = disnake.ui.View()

        # Создаем кнопки confirm и cancel
        confirm_button = disnake.ui.Button(style=disnake.ButtonStyle.green, label="Confirm", custom_id='Confirm')
        cancel_button = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Cancel", custom_id='Cancel')

        view.add_item(confirm_button)
        view.add_item(cancel_button)
        user_uval = inter.author.mention
        user_uval2 = inter.author.id
        user_uval1 = embed.fields[0].value
        user_prichina = embed.fields[3].value
        # if 1119326877820133496 or 1119326877807554683 or 1119326877820133497 or 1139165924826562660 in [role.id for role in reversed(inter.author.roles)]:
        #     await inter.response.send_message(
        #         f'<@&1119326877820133504> <@&1119326877820133503>\nПришло заявление от {inter.author.mention}',
        #         embed=embed, view=view)
        embed1 = embed
        main_channel = bot.get_channel(1174110990846148749)
        await main_channel.send(
            f'123\n<@&1119326877820133502> <@&1121421400540975134>\nПришло заявление от {inter.author.mention}',
            embed=embed1, view=view)
        global main_message
        main_message = bot.get_message(main_channel.last_message.id)
        await inter.response.send_message()
        message_url = inter.message.jump_url

        @bot.listen("on_button_click")
        async def qwewqe(inter: disnake.MessageInteraction):
            if inter.component.custom_id == "Cancel":
                await inter.response.send_modal('1123123')

        # Ожидаем нажатия кнопки
        # def check(ctx):
        #     return (ctx.message.id == main_message
        #             and ctx.component.label in ["Confirm", "Cancel"]
        #             and role_id in [role.id for role in ctx.user.roles]
        #     )
        #
        # try:
        #     interaction = await bot.wait_for("button_click", check=check, timeout=None)
        # except disnake.NotFound:
        #     return
        #
        # # Обновляем сообщение после нажатия кнопки
        # if interaction.component.label == "Confirm":
        #     view = disnake.ui.View()
        #     new_button = disnake.ui.Button(emoji='✔️', disabled=True, style=disnake.ButtonStyle.success, row=0)
        #     new_button2 = disnake.ui.Button(label='Рассмотрел', disabled=True,
        #                                     style=disnake.ButtonStyle.secondary, row=1)
        #     new_button3 = disnake.ui.Button(label=f'{interaction.author.display_name}', disabled=True,
        #                                     style=disnake.ButtonStyle.secondary, row=1)
        #     view.add_item(new_button)
        #     view.add_item(new_button2)
        #     view.add_item(new_button3)
        #     await main_message.edit(view=view)
        #     await interaction.response.edit_message(view=view)
        #     channel_id = 1123565649352986644  # Замените на ID вашего текстового канала
        #     channel = bot.get_channel(channel_id)
        #
        #     embed = disnake.Embed(
        #         color=disnake.Color.dark_grey(),
        #         timestamp=datetime.datetime.now(),
        #     )
        #
        #     embed.set_author(
        #         name="Кадровый аудит",
        #     )
        #
        #     embed.add_field(name='', value=f"1. {interaction.author.display_name}  {interaction.author.mention}",
        #                     inline=False)
        #     embed.add_field(name='', value=f"2. {user_uval1}  {user_uval}", inline=False)
        #     embed.add_field(name='', value="3. Уволен", inline=False)
        #     embed.add_field(name='', value=f"4. {user_prichina}  {message_url}", inline=False)
        #     embed.set_footer(
        #         text="by x1she",
        #         icon_url="https://cdn.discordapp.com/attachments/969288747059412993/1174123812300783732/KaCuSJIkm4DiSZSUp78Q7BTDceasYve2ZnXZ_W-IUxGVDaPX9b2eQKEeg93DFEzChMRMA-uuhM7-fVoIPes_mow.jpg?ex=65667303&is=6553fe03&hm=7f72a6a508f6b7375315684ea75ddeab97627f9afa46137c390b72e90e89536c&",
        #     )
        #     await channel.send(embed=embed)
        #     if interaction.author.top_role > inter.guild.get_member(user_uval2).top_role:
        #         embed_uval_sms1 = disnake.Embed(
        #             title="Ваше заявление на увольнение было одобренно",
        #             description="Вы были автоматически кикнуты с сервера Goverment",
        #             color=disnake.Colour.dark_blue(),
        #             timestamp=datetime.datetime.now(),
        #         )
        #         embed_uval_sms1.set_thumbnail(
        #             url="https://cdn.discordapp.com/attachments/969288747059412993/1174123812300783732/KaCuSJIkm4DiSZSUp78Q7BTDceasYve2ZnXZ_W-IUxGVDaPX9b2eQKEeg93DFEzChMRMA-uuhM7-fVoIPes_mow.jpg?ex=65667303&is=6553fe03&hm=7f72a6a508f6b7375315684ea75ddeab97627f9afa46137c390b72e90e89536c&")
        #         embed_uval_sms1.add_field(name="Пользователь ответивший на заявку",
        #                                   value=f"{interaction.author.mention} - {interaction.author.display_name}",
        #                                   inline=False)
        #         embed_uval_sms1.add_field(name="Ссылка на заявку", value=f"{message_url}", inline=False)
        #         embed_uval_sms1.set_footer(
        #             text="by x1she",
        #             icon_url="https://cdn.discordapp.com/attachments/969288747059412993/1174123812300783732/KaCuSJIkm4DiSZSUp78Q7BTDceasYve2ZnXZ_W-IUxGVDaPX9b2eQKEeg93DFEzChMRMA-uuhM7-fVoIPes_mow.jpg?ex=65667303&is=6553fe03&hm=7f72a6a508f6b7375315684ea75ddeab97627f9afa46137c390b72e90e89536c&",
        #         )
        #
        #         await inter.guild.get_member(user_uval2).send(embed=embed_uval_sms1)
        #         await inter.guild.get_member(user_uval2).kick(reason=None)
        # elif interaction.component.label == "Cancel":
        #     print('eblan')
        #     view = disnake.ui.View()
        #     new_button = disnake.ui.Button(label="❌", disabled=True, style=disnake.ButtonStyle.danger, row=0)
        #     new_button2 = disnake.ui.Button(label='Рассмотрел', disabled=True,
        #                                     style=disnake.ButtonStyle.secondary, row=1)
        #     new_button3 = disnake.ui.Button(label=f'{interaction.author.display_name}', disabled=True,
        #                                     style=disnake.ButtonStyle.secondary, row=1)
        #     view.add_item(new_button)
        #     view.add_item(new_button2)
        #     view.add_item(new_button3)
        #     await main_message.edit(view=view)
        #     await interaction.response.edit_message(view=view)
        #     embed_uval_sms = disnake.Embed(
        #         title="Ваше заявление на увольнение было отклонено",
        #         color=disnake.Colour.dark_blue(),
        #         timestamp=datetime.datetime.now(),
        #     )
        #     embed_uval_sms.set_thumbnail(
        #         url="https://cdn.discordapp.com/attachments/969288747059412993/1174123812300783732/KaCuSJIkm4DiSZSUp78Q7BTDceasYve2ZnXZ_W-IUxGVDaPX9b2eQKEeg93DFEzChMRMA-uuhM7-fVoIPes_mow.jpg?ex=65667303&is=6553fe03&hm=7f72a6a508f6b7375315684ea75ddeab97627f9afa46137c390b72e90e89536c&")
        #     embed_uval_sms.add_field(name="Пользователь ответивший на заявку",
        #                              value=f"{interaction.author.mention} - {interaction.author.display_name}",
        #                              inline=False)
        #     embed_uval_sms.add_field(name="Ссылка на заявку", value=f"{message_url}", inline=False)
        #     embed_uval_sms.set_footer(
        #         text="by x1she",
        #         icon_url="https://cdn.discordapp.com/attachments/969288747059412993/1174123812300783732/KaCuSJIkm4DiSZSUp78Q7BTDceasYve2ZnXZ_W-IUxGVDaPX9b2eQKEeg93DFEzChMRMA-uuhM7-fVoIPes_mow.jpg?ex=65667303&is=6553fe03&hm=7f72a6a508f6b7375315684ea75ddeab97627f9afa46137c390b72e90e89536c&",
        #     )
        #
        #     await inter.guild.get_member(user_uval2).send(embed=embed_uval_sms)


bot.run(
    'your_bot_token')  # Замените 'your_bot_token' на токен вашего бота
