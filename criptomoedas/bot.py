import requests
import discord
import time
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}.')
    canal_btc = client.get_channel(1071469072094609410) # id do canal bitcoin
    canal_eth = client.get_channel(1071478508418773082) # id do canal ethereum
    canal_ltc = client.get_channel(1071483050661261323) # id do canal litecoin
    canal_sol = client.get_channel(1071490515754827856) # id do canal solana
    canal_usd = client.get_channel(1071494195547754596) # id do canal usdc / usdt
    while True:
        a = "462b13fe-538b-4ca9-8730-8102a99dd1cc";b = "b194638b-b9f2-4189-9781-88cf0b32c32e"
        c = "b880c2da-b462-4374-8d6e-72213b864bb9";d = "314bc812-fad4-4ed2-9982-9f51b0121eb8"

        # Bitcoin
        respostabrl = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=BRL&CMC_PRO_API_KEY={a}").json()
        respostausd = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD&CMC_PRO_API_KEY={a}").json()
        bitcoin_price_brl = respostabrl["data"]["BTC"]["quote"]["BRL"]["price"]
        bitcoin_price_usd = respostausd["data"]["BTC"]["quote"]["USD"]["price"]
        price_brl_formatted = locale.currency(bitcoin_price_brl, grouping=True, symbol=True)
        price_usd_formatted = locale.currency(bitcoin_price_usd, grouping=True, symbol=False)
        embed_btc = discord.Embed(title="Bitcoin Price", description=f"BRL: `{price_brl_formatted}`\nUSD: `{price_usd_formatted}$`", color=0x00FF00)
        embed_btc.set_thumbnail(url="https://cdn3.emoji.gg/emojis/4586-bitcoin-logo.png")
        await canal_btc.send(embed=embed_btc)

        # Ethereum
        respostabrl = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=ETH&convert=BRL&CMC_PRO_API_KEY={b}").json()
        respostausd = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=ETH&convert=USD&CMC_PRO_API_KEY={b}").json()
        eth_price_brl = respostabrl["data"]["ETH"]["quote"]["BRL"]["price"]
        eth_price_usd = respostausd["data"]["ETH"]["quote"]["USD"]["price"]
        eth_price_brl_formatted = locale.currency(eth_price_brl, grouping=True, symbol=True)
        eth_price_usd_formatted = locale.currency(eth_price_usd, grouping=True, symbol=False)
        embed = discord.Embed(title="Ethereum Price", description=f"BRL: `{eth_price_brl_formatted}`\nUSD: `{eth_price_usd_formatted}$`", color=0x00FF00)
        embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/7675-ethereum.png")
        await canal_eth.send(embed=embed)

        # Litecoin
        respostabrl = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=LTC&convert=BRL&CMC_PRO_API_KEY={c}").json()
        respostausd = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=LTC&convert=USD&CMC_PRO_API_KEY={c}").json()
        ltc_price_brl = respostabrl["data"]["LTC"]["quote"]["BRL"]["price"]
        ltc_price_usd = respostausd["data"]["LTC"]["quote"]["USD"]["price"]
        ltc_price_brl_formatted = locale.currency(ltc_price_brl, grouping=True, symbol=True)
        ltc_price_usd_formatted = locale.currency(ltc_price_usd, grouping=True, symbol=False)
        embed = discord.Embed(title="Litecoin Price", description=f"BRL: `{ltc_price_brl_formatted}`\nUSD: `{ltc_price_usd_formatted}$`", color=0x00FF00)
        embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/4887-ltc.png")
        await canal_ltc.send(embed=embed)

        # Solana
        respostabrl = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=SOL&convert=BRL&CMC_PRO_API_KEY={d}").json()
        respostausd = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=SOL&convert=USD&CMC_PRO_API_KEY={d}").json()
        sol_price_brl = respostabrl["data"]["SOL"]["quote"]["BRL"]["price"]
        sol_price_usd = respostausd["data"]["SOL"]["quote"]["USD"]["price"]
        sol_price_brl_formatted = locale.currency(sol_price_brl, grouping=True, symbol=True)
        sol_price_usd_formatted = locale.currency(sol_price_usd, grouping=True, symbol=False)
        embed = discord.Embed(title="Solana Price", description=f"BRL: `{sol_price_brl_formatted}`\nUSD: `{sol_price_usd_formatted}$`", color=0x00FF00)
        embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/7187-solana.png")
        await canal_sol.send(embed=embed)

        # USDC / USDT
        respostabrl = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=USDT&convert=BRL&CMC_PRO_API_KEY={d}").json()
        respostausd = requests.get(f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=USDT&convert=USD&CMC_PRO_API_KEY={d}").json()
        usd_price_brl = respostabrl["data"]["USDT"]["quote"]["BRL"]["price"]
        usd_price_usd = respostausd["data"]["USDT"]["quote"]["USD"]["price"]
        usd_price_brl_formatted = locale.currency(usd_price_brl, grouping=True, symbol=True)
        usd_price_usd_formatted = locale.currency(usd_price_usd, grouping=True, symbol=False)
        embed = discord.Embed(title="USDC / USDT Price", description=f"BRL: `{usd_price_brl_formatted}`\nUSD: `{usd_price_usd_formatted}$`", color=0x00FF00)
        embed.set_thumbnail(url="https://cryptologos.cc/logos/tether-usdt-logo.png")
        await canal_usd.send(embed=embed)

        time.sleep(5000) # delay em segundos para cada consulta e envio dos valores

client.run("") # token do bot
