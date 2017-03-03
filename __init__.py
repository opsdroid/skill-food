import random
import aiohttp

from opsdroid.matchers import match_regex


@match_regex(r".*(w|W)(h)?at.*(should|shall) (I|i).*eat(\?)?")
async def whatshallieat(opsdroid, config, message):

    listoffood = [
        "How should I know I'm a machine!",
        "How about a packet of crisps!",
        "What about some sandwiches?",
        "You should have karela in your curry."
    ]

    url = "http://food2fork.com/api/search?key={}&q=".format(config.get("api-key"))

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                recipes = await resp.json()
                my_recipe = random.choice(recipes["recipes"])
                await message.respond("How about {}?".format(my_recipe["title"].lower()))
                await message.respond(my_recipe["image_url"])
            else:
                await message.respond(random.choice(listoffood))
