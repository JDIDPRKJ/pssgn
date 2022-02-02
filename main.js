const { Embed } = require('@discordjs/builders')
const { Client, Intents, MessageEmbed } = require('discord.js')
const fs = require('fs')
require('dotenv').config()
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] })

let prefix = '/'

client.on('ready', async bot => 
{
    console.log(`Bot listo, iniciado en ${bot.user.username}#${bot.user.discriminator} - ${bot.presence.status}`)
    bot.user.setActivity('Okee JDI Bot', { type: 'PLAYING' })
})

const me = new MessageEmbed().setColor([0, 0, 255]).setTitle('Pong').setAuthor('Comando Pong', 'https://www.debate.com.mx/__export/1433389739908/sites/debate/img/ahora/2015/06/03/perro-militar-entrenado-600x330.jpg_219914347.jpg', 'https://www.discord.com/')

client.on('message', async message =>
{
    const args = message.content.slice(prefix.length).split(/ +/)
    const command = args.shift().toLowerCase('')

    if(message.author.bot) return
    
    switch(command)
    {
        case 'ping':
            message.reply('Pong')
    }
})

client.login(process.env.BOT_TOKEN)
