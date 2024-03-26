import asyncio
import os
import random

import discord

class QuizBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.quiz_data = {
            "Foundation": {  # Define question pool for the "Foundation" quiz type
                "An amateur radio licence may be used for  A. Advertising a retailer of amateur radio equipment B. Controlling a fleet of taxis C. Testing propagation between two amateurs in different countries D. Providing radio communications for a commercial fairground operator ":
                "C",
                "HF propagation is NOT affected by the A. sun. B. time of day. C. day of the week. D. frequency used. ":
                "C",
                "Which of the following is a foundation licence holder NOT allowed to do? A. Operate a radio transmitter that the licence holder has designed themselves. B. Design and operate a radio receiver. C. Assemble and operate a transmitter designed by an intermediate licence holder D.  Assemble and operate a radio deigned by a commercial company ":
                "A",
                "An amateur radio licence holder must, when changing the main station address, immediately notify A. the local police. B. the local council. C. the RSGB. D. Ofcom. ":
                "D",
                "When transmitting, you must give your call sign A. When establishing contact and at least every 5 minutes B. When establishing contact and as frequently as is practicable. C. During CQ calls and at the beginning and end of the contact D. At the beginning and end of the contact. ":
                "B",
                "A Foundation licence holder, operating under the supervision of a Full licence holder and using the Full licence holders callsign, must  A. operate subject to the restrictions of the Foundation licence. B. operate in accordance with the supervisors licence. C. ensure that any contacts are recorded in the log. D. reduce the transmitters power to 10 watts. ":
                "B",
                "You are talking to M3ABC by amateur radio and some friends enter his room. You may also address remarks to these friends A. if they are family members. B. if M3ABC gives permission. C. if they are also licenced radio amateurs. D. but only on the calling channel. ":
                "C",
                "Which of the following may NOT be used in an amateur radio transmission? A. A message sent in Morse code B. A message sent containing Q codes. C. A message using secret codes known only to the sender and recipient. D. A message containing data. ":
                "C",
                "A Foundation licence holder may operate in a foreign country if A. this is within the European Union. B. operating in that countries coastal waters C. the country recognises UK amateur radio licences D. given permission by the appropriate authority of that country ":
                "D",
                "Which part of an amateur band is not permitted within 100km of Charing Cross, London? A.  1·810-1·830MHz B.  51·00-52·00MHz C.  431·0-432·0MHz D.  438·0-440·0MHz ":
                "C",
                "To whom do EMF restrictions apply? A.  Members of the general public. B.  Foundation licence holders. C.  Intermediate licence holders. D.  Full licence holders ":
                "A",
                "Which of the following is a good conductor of an electric current? A. Rubber B. Plastic C. Glass D. Aluminium ":
                "D",
                "In a circuit of resistors in series that are connected to a battery, the current flowing each resistor will A. be the same as the battery voltage. B. be different depending on the voltage of the battery. C. be different depending on the value of the resistor. D. be same in each resistor. ":
                "D",
                "A 12V mobile transceiver consumes 10W on receive and 100W on transmit. The highest current drawn will be A. 0.83A B. 0.83Ω C. 8.3A D. 8.3Ω ":
                "C",
                "The correct formula relating the voltage, V,  the current, I, and the resistance R is A. R = V - I B. R = V × I C. R = I / V D. R = V / I ":
                "D",
                "The voltage across three resistors connected in series is 5 volts, 10 volts and 20 volts respectively. The total voltage across all three resistors is A. 5 volts B. 10 volts. C. 20 volts. D. 35 volts. ":
                "D",
                "Which of the following will work normally when connected to a battery of the correct voltage regardless of battery polarity? A. Incandescent lamp B. Radio receiver C. LED lamp D. Pocket Calculator ":
                "A",
                "What is the significant difference between AC and DC? A. Direct currents are always greater than alternating currents. B. Direct currents take a long time to change direction. C. Alternating currents are continually changing direction. D. Alternating currents have a fixed polarity ":
                "C",
                "The frequency 50MHz is A. LF B. HF C. VHF D. UHF ":
                "C",
                "A frequency of 100 MHz has a wavelength of A. 3 metres. B. 30 metres. C. 0.3 metres. D. 300 metres. ":
                "A",
                "Digital signals are A. constantly changing in amplitude B. astream of finite values at a specific sampling interval. C. totally immune to interference. D. created by a Digital to Analogue converter. ":
                "B",
                "An Analogue to Digital Converter (ADC) A. represents a digitial signal in analogue format  B. samples an analogue signal and creates a digital representation of it C. changes audio signals to RF D. is an optional component in a Software defined radio ":
                "B",
                "A secondary battery A. cannot be  recharged. B. may be recharged. C. undergoes a chemical process that cannot be reversed. D. consists of a single cell. ":
                "B",
                "Adding information to a radio frequency carrier is known as A. transmission. B. tuning. C. amplification. D. modulation. ":
                "D",
                "Audio or data information is combined with  a radio frequency carrier in which stage of a transmitter? A. Microphone Amplifier. B. Modulator. C. RF Power amplifier. D. AF power amplifier. ":
                "B",
                "When radio frequencies are mixed with audio frequencies, the new frequencies that are generated are called A. fundamentals B. harmonics C. sidebands D. carriers ":
                "C",
                "Incorrect setting of the oscillator in a transmitter may cause A. damage to the power supply. B. distortion to the transmitted signal. C. damage to the antenna. D. transmitting on the wrong frequency. ":
                "D",
                "If the microphone gain is set too high on a transmitter A. the antenna could be damaged. B. interference could be caused on adjacent channels. C. the supply fuse will fail D. the operator could get an electric shock from the microphone ":
                "B",
                "The RF power amplifier A. takes the signal from the microphone and amplifies it to a suitable level B. amplifies the low power modulated radio signal to suitable level to feed the antenna C. converts the mains supply to a suitable voltage to be used by the transmitter D. ensures the transmitter is radiating on the correct frequency. ":
                "B",
                "If the transmitters RF power amplifier output is not connected to a correctly matched antenna A. the antenna can be damaged. B. SWR will be too low. C. interference will be caused on adjacent channels. D. the transmitter can be damaged. ":
                "D",
                "Too much audio gain is likely to cause a transmitter to A. stop working. B. Increase the SWR. C. interfere with other bands. D. interfere with adjacent frequencies. ":
                "D",
                "Recovering the original information from a received radio signal is called A. demodulation. B. modulation. C. filtering. D. oscilating. ":
                "A",
                "In a receiver, the demodulator A.  recovers the original information from the received signal. B. amplifies the received signal so that it can be heard through the loudspeaker. C. mixes the audio signal with the frequency from the local oscilator. D. matches the antenna to the transmitter. ":
                "A",
                "In a Software Defined Radio, demodulation is carried our by A. a diode detector B. the RF amplified C. the local oscilator D. mathematical processes ":
                "D",
                "A twin feeder cable A. can be burried underground to prevent interference. B. is balanced having equal and opposite signals in each wire. C. is unbalanced with one wire at ground and the other carrying the signal. D. has greater loss than a coaxial cable. ":
                "B",
                "Loss in feeders increases with A. the modulation used B. length of the feeder cable C. lower transmit frequencies D. higher gain antennas ":
                "B",
                "A balun is primarily used to  A. increase the power fed to the antenna B. decrease the power fed to the antenna C. connect an unbalanced feeder to a balanced antenna D. protect against damage caused by static electricity ":
                "C",
                "A vertical half wave dipole will radiate A. equally in all horizontal directions. B. a maximum signal in a vertical direction. C. a minimum signal at right-angles to the antenna. D. a maximum signal oﬀ the ends of the antenna. ":
                "A",
                "The gain of an antenna is measured in A. Watts. B. Volts. C. Amps. D. dB. ":
                "D",
                "6.1W ERP is equivalent to A. 6W. B. 6W EIRP. C. 10W EIRP. D.10W. ":
                "C",
                "For best reception of UHF or VHF signals the antennas of both receiver and transmitter should both be  A. vertical. B. horizontal. C. in the same orientation. D. in any orientation. ":
                "C",
                "The feed point impedance of an antenna is related to A. the cable used to connect to the antenna. B. the mode of transmission. C. the output power of the transmitter. D. the dimensions of the antenna and the wavelength of the applied signal. ":
                "D",
                "An amateur changes band of operation but does not check the antenna is still matched. This might cause A. high levels of Standing Waves in the feeder. B. distortion of the transmitted signal. C. antenna overloading. D. interference to be caused on other bands. ":
                "A",
                "In a well designed and matched antenna system, measured SWR at the transceiver will be A. > 5 1 B. > 3 1 C. 2 1 D. < 1.5 1 ":
                "D",
                "If an antenna is being used on a frequency for which it has not been designed A. measured SWR will be very low. B. antenna matching will be required. C. interference may be caused to adjacent channels D. the antenna could be damaged. ":
                "B",
                "A dummy load is A. a weight used to obtain the correct tension on a long wire antenna B. a screened resistor that may be connected to the transmitter output without radiating C. a suitable resistor to connect to the power supply when the transmitter is disconnected D. used instead of the microphone when using a transceiver to receive only ":
                "B",
                "The connector shown is a A. jack plug. B. PL259. C. SO238. D. BNC. ":
                "D",
                "Radio waves A. maintain their power as they propagate. B. normally travel in straight lines. C. always pass through the ionosphere. D. never pass through the ionosphere. ":
                "B",
                "Propagation of VHF and UHF frequencies is normally A. decreased with sporadic E B. refracted back to earth by the troposphere. C. not much beyond the  line of sight. D. not possible beyond the ionosphere. ":
                "C",
                "The lowest layer of the ionosphere is at a height of about A. 800km B. 700m C. 70km D. 10km ":
                "C",
                "VHF/UHF signals A. are unaffected by buildings B. become weaker as they pass through buildings. C. become stronger at higher frequencies D. are unaffected by atmospheric conditions. ":
                "B",
                "Snow, ice and rain have the most detrimental effect on which frequency range? A. LF B. HF C. VHF D. UHF ":
                "D",
                "A VHF transmitting antenna should be located  A. indoors B. outdoors C. close to the transmitter so you can easily adjust it to the correct length. D. at ground level to minimise interference. ":
                "B",
                "Electromagnetic compatibility (EMC) means  A. the antenna is properly matched to the transmitter. B. the avoidance of interference between electronic equipment. C. ensuring electronic equipment generates small electromagnetic fields. D. amicrophone will work correctly when connected to a transmitter. ":
                "B",
                "A radio amateur’s transmission is LEAST likely to cause interference to A. other amateurs. B. other radio users. C. an electric drill. D. an electronic security alarm. ":
                "C",
                "An amateur radio transmitter can cause electromagnetic interference to A. electric drills. B. vacuum cleaners. C. lawn mowers. D. electronic equipment ":
                "D",
                "Which of the following will NOT cause interference with the operation of a radio receiver? A. A lawn mower. B. An electric drill. C. Central heating controls. D. A SWR meter. ":
                "D",
                "Which of the following will NOT  lead to an increase in risk of causing electromagnetic interference? A. Changing from SSB to FM transmission. B. Increasing the transmit power. C. Changing from PSK to Morse code transmission. D. Increasing the microphone gain. ":
                "A",
                "Which of the following is least likely to provide a route of entry of interference into domestic TV equipment. A. Feeder from the antenna to the transmitter. B. Electronic components inside the TV. C. Audio speaker leads. D. RF earth rod. ":
                "D",
                "Immunity to interference from most sources can be increased by A. Fitting chokes and filters in mains or antenna leads. B. Using longer mains leads to the TV. C. Fitting a preamplifier to the TV antenna input. D. Fitting a higher rated fuse to the TV plug. ":
                "A",
                "A dummy load is used A. to test if RF signals are being conducted out of a transmitter through its power cables. B. to test the power being sent to the headphones in a receiver C. to match an aerial to a feeder D to test the setting of the microphone gain on the transmitter. ":
                "A",
                "EMC problems can be minimised by A. using end fed long wire antennas. B. locating antennas as close as possible to houses. C. siting antennas as high and as far away from houses as possible. D. using loft antennas. ":
                "C",
                "An RF earth terminal of a transmitter should be connected to A. the metal pipework in the central heating system. B. the earth pin of the mains plug. C. the mains earth at the fuse box . D. a long copper rod buried in damp ground. ":
                "D",
                "When fitting a transceiver in a vehicle, whose reasonability is it to ensure that the installation is in accordance with  vehicles electrical and management systems? A. The vehicle owner. B. The police. C. The driver's insurance company. D. The transceiver manufacturer. ":
                "A",
                "After fitting a transceiver in a vehicle, testing of the installation A. should be done with the vehicle stationary and all vehicles electrical systems running. B. should be done with the vehicle moving on the road and with all vehicle electrical systems running. C. is not required. D. is only required if specified by the vehicles insurers. ":
                "A",
                "Which of the following is most likely to cause problems to an amateur radio receiver in a vehicle? A. Ignition Systems. B. Headlights control. C. Brake Lights. D. Automatic gearbox. ":
                "A",
                "Your neighbour comes to your door and complains that the interference he is getting on his TV is being caused by your radio transmissions. You should A. offer to carry out test transmissions with his co-operation to verify his allegation. B. explain that it cannot be your radio transmissions as your equipment is 'CE' approved C. advice him to contact Ofcom for advice D. request that he comes to you with proof of his allegation. ":
                "A",
                "A good reason for keeping a log of all transmission is because A. It will make it easier to check allegations of interference. B. it is required by Ofcom. C. it is a requirement of the amateur radio licence. D. it will help support an application for planning permission for an antenna. ":
                "A",
                "Before transmitting you should first listen on a frequency and then ask if the frequency is clear because A. the frequency may be in use but one of the stations may be in a location where you can't receive their signal. B. it is a requirement of the amateur radio licence. C. this lets other amateur radio operators know that you are about to commence a QSO. D. it is considered to be polite to commence all new QSO's in this way. ":
                "A",
                "When calling  CQ, this is M7ABC calling CQ on 20 meters  you should A. repeat the sequence several times in quick succession over a period of 20 - 30 seconds B. call the sequence once and then listen for several seconds in between each C. repeat the sequence several times in quick succession D. repeat the sequence several times in quick succession":
                "Correct answer.",
                "Correct answer. 7A3 A. remain on the frequency until another station wishes to use it. B. remain on the frequency as long as the contact takes. C. ask if the frequency is clear.":
                "",
                "Once you have contacted another station on a VHF FM calling channel you should A. remain on the frequency until another station wishes to use it. B. remain on the frequency as long as the contact takes. C. ask if the frequency is clear. D. change frequency to a suitable clear channel. ":
                "D",
                "The correct phonetic spelling of ‘SIGNAL’ is A. SIERRA ITALY GOLF NOVEMBER APPLE LIMA B. SIERRA ITALY GOLF NORWAY ALPHA LIMA C. SIERRA INDIA GOLF NOVEMBER ALPHA LIMA D. SUGAR INDIA GOLF NOVEMBER ALPHA LIMA ":
                "C",
                "If hearing bad language or inappropriate behaviour on air you should A. ignore it without comment and do not refer to it on air. B. ignore it and warn people on air on other frequencies to avoid it. C. reprimand the person responsible over the air. D. complain to the local council. ":
                "A",
                "Band plans are used because A. using them is a condition of the licence. B. they help prevent on-air abuse. C. they enable efficient use of the band for diﬀerent modes. D. they are required for radio competitions ":
                "C",
                "A badly setup transmitter operating on 50.1 MHz is also radiating on 150.3MHz. Which service might be affected? A. Broadcast Radio B. Aeronautical mobile C. Radio Astronomy D. Maritime Mobile ":
                "C",
                "A 2m repeater transmits on 145.600MHz. To which frequency should you tune your transmitter in order to use this repeater? A. 146.200MHz B. 145.600MHz C. 145.000MHz D. 144.000MHz ":
                "C",
                "If using a microphone, other than the one supplied with the transceiver you should A. ensure that the PTT and audio levels are correct. B. use a separate PTT switch. C. use a separate microphone pre-amplifier. D. re-check the SWR. ":
                "A",
                "You are having a contact (QSO) with another amateur and he reports your signal as ‘5 and 5’. This means that he is reading your transmission  A. Excellent audio and very strong signal strength B. Average audio and a very strong signal strength C. Excellent Audio with an average signal strength D. Average Audio with an average signal strength ":
                "C",
                "Digital Voice (DV) radios A. may have the owners callsign embedded in the configuration. B. are interoperable across all systems. C. automatically check to see if a channel is in use. D. cause more interference than SSB radios ":
                "A",
                "When using FM or DV at 145.550 MHz you should first A. check if the repeater is being used for other modes. B. open the receiver squelch and check for other modes. C. ask if the frequency is in use and listen for a reply. D. wait till you hear the repeater’s callsign and then call with your callsign. ":
                "B",
                "Terrestrial contacts on the portion of the amateur bands shown as allocated to satellites A. are strongly discouraged. B. should be used with vertical polarisation. C. must be used with horizontal polarisation. D. cannot be used during daylight. ":
                "A",
                "A linear amplifier has a high voltage section running at 1200 volts at 500mA the potential danger through misuse is A. Electrocution. B. Fire. C. Lightning. D. Interference. ":
                "A",
                "When using mains powered equipment A. it should be connected to a safety earth B. the safety earth must be connected to the RF earth. C. the safety earth becomes unnecessary D. the RF earth becomes unnecessary. ":
                "A",
                "The correct way to wire a UK 3-pin plug is A. Green/Yellow to Earth B. Brown to Earth C. Brown to Earth D. Green/Yellow to Earth":
                "A",
                "In the event that a fuse blows you should A. find out the cause of the problem. B. replace the fuse with one of a higher rating. C. measure the voltage across the fuse. D. return the affected equipment to the place of purchase. ":
                "A",
                "A Residual Current Circuit Breaker with Overcurrent Protection (RCBO) will stop mains power in a circuit  A. Only when there is a current leakage to earth above its leakage threshold. B. Only when there is an excessive current in the circuit above the current threshold. C. When there is both earth leakage and excessive current above the device threshold. D. When there is either earth leakage or excessive current above the device threshold. ":
                "D",
                "When carrying out maintenance or repair work on electronic equipment you should A. follow the manufacturers guidelines for servicing the equipment. B. ensure that the correct fuse is fitted to the mains plug. C. ensure that part of you is in contact with the metal chassis. D. have someone else present with you in the room. ":
                "A",
                "The mains power switch to the radio shack should be A. difficult to reach. B. key operated to prevent use by non-licensed persons. C. switched oﬀ at all times. D. in a clearly marked position ":
                "D",
                "One feature of Nicad (NiCad), Nickel Metal Hydride (NIMH) and Lithium batteries is that A. they all have different charging requirements and must only be used with the recommended charger. B. the terminal voltages are all the same allowing almost any charger to be safely used.  C  they may be safely discarded in the household waste or a litter bin in the street. D. they must be kept fully charged at all times to ensure a long life. ":
                "A",
                "When using power tools it is A. advisable to wear eye protection. B. advisable to wear ear protection. C. essential to wear breathing protection. D. essential to wear gloves. ":
                "A",
                "What safety considerations should you bear in mind when using power tools rather than hand tools? A. Power tools can do more damage and don’t stop instantly. B. Power tools can produce a neater and more accurate job. C. It is a lot less effort when using power tools. D. The job can be completed much more quickly. ":
                "A",
                "Soldering work stations  A. Require an emergency cut oﬀ switch in case the soldering tip comes into contact with the skin. B. Should be well ventilated to avoid inhaling fumes. C. Must be on an anti-static surface. D. Must be earthed. ":
                "B",
                "Why should two people be present during antenna erection? A. Because working at heights is risky and someone my be needed to fetch help. B. Because there needs to be someone on the ground who can see what needs doing. C. Because it saves constantly going up and down the ladder to read the SWR meter. D. Because the person doing the work will often need a hand. ":
                "A",
                "Overreaching when on a ladder may cause A. concern to passers by B. the person to fall off the ladder C. a hard hat to give less protection D. a poorly constructed or loose fitting job ":
                "B",
                "The main purpose of wearing a tool belt when up a ladder is to A. prevent the tools being damaged B. provide a strong belt to tie to the ladder for safety C. avoid having to repeatedly climb the ladder D. reduce the risk of dropping tools ":
                "D",
                "Which part of the body is MOST susceptible to the effect of exposure to electromagnetic radiation? A. The arms. B. The torso. C. The head. D. The eyes. ":
                "D",
                "The ICNIRP is of interest to amateurs because it A. oversees the preparation of the International Radio Regulations B. produces guidance on the safe levels of RF exposure C. co-ordinates the launch of amateur and other satellites D. produces the International version of the Amateur Band Plans ":
                "B",
                "The main risk when looking down waveguides is that A. microwave radiation could overheat your eye B. waveguides have very sharp edges and can cut C. you could be accidentally stabbed in the eye D. dust and small particles could be blown into the eyes ":
                "A",
                "Antennas connected to transmitting equipment A. should be mounted where they cannot accidentally be touched when in use. B. should be placed where they can easily be manually adjusted. C. must be connected with the shortest possible feeder. D. always require an antenna matching unit. ":
                "A",
                "When installing antennas high above the ground or in areas of high elevation A. measures should be taken to protect against lightning. B. warning lights should be fitted at the top to warn aircraft. C. twin feeder should be used. D. the mast should be insulated from the ground. ":
                "A",
                "When working a portable field station, feeder cables must be A. as long as possible. B. located away from overhead power cables. C. run along the ground to the antenna mast. D. as short as possible ":
                "B",
                "When operating a portable station A. care should be taken to avoid trailing wires. B. asuitable amperage fuse should be installed at the generator to avoid electrocution. C. the local council should be informed D. Residual Current Circuit Breakers are not required. ":
                "A",
                "Using excessive volume when wearing headphones can result in A. complaints from neighbours about the noise B. damage to your transmitter C. overloading your receiver D. damage to your hearing ":
                "D",
                "What of the following features should you consider when demonstrating amateur radio to a group of scouts and guides at their church hall to maximise safety? A. The location of antenna feeders and power cables. B. The seating arrangements so everybody has a good view. C. Sufficient club members to watch the presentation. D. The use of desk microphones rather than hand held. ":
                "A",
                "Who at a radio club meeting is responsible for the general health and safety of the club members and any visitors? A. All club members present. B. Each is responsible for themselves. C. The club chairman. D. The club safety officer ":
                "A",
                "You are visiting your friend who is a Full licence holder and using his transmitter at 200 watts. Your friend leaves the room. You may continue operating A. at 200 Watts because your friend is supervising you using a hand-held B. at 200 Watts because your friend is still on the premises C. at the same power but must use your own callsign D. but must use your own callsign and licence conditions.":
                "D",
                "You answer a CQ call which is calling for a contact in your home town. You are then asked to pass on a message to a person who may not be an amateur. You may A. not pass the message under any circumstances B. pass the message if it relates to an international disaster C. pass the message if the originator or recipient is an amateur D. pass the message if the originator is an amateur.":
                "B",
            },
            "Intermediate": {  # Define question pool for the "Intermediate" quiz type
                "Question 1": "Answer 1",
                "Question 2": "Answer 2",
                # Add more questions and answers here
            },
            "Full": {  # Define question pool for the "Full" quiz type
                "Question 1": "Answer 1",
                "Question 2": "Answer 2",
                # Add more questions and answers here
            },
        }

    async def start_quiz(self, message, quiz_type):
        quiz_type = quiz_type.capitalize()
        if quiz_type not in self.quiz_data:
            await message.channel.send(f"Quiz type '{quiz_type}' not found.")
            return

        question_pool = self.quiz_data[quiz_type]
        question, answer = random.choice(list(question_pool.items()))

        await message.channel.send(question)

        def check(m):
            return m.author == message.author and m.content.lower() == answer.lower()

        try:
            response = await self.wait_for('message', timeout=20.0, check=check)
            await message.channel.send(
                f'Correct! {message.author.mention} got it right. It was: {answer}!')
        except asyncio.TimeoutError:
            await message.channel.send(
                f'Sorry, time is up! The correct answer was: {answer}')

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!quiz'):
            # Extract quiz type from the message content
            parts = message.content.split()
            if len(parts) < 2:
                await message.channel.send("Please specify a quiz type.")
                return
            quiz_type = parts[1]

            await self.start_quiz(message, quiz_type)


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = QuizBot(intents)

    try:
        token = os.getenv("TOKEN") or ""
        if token == "":
            raise Exception("Please add your token to the Secrets pane.")
        bot.run(token)
    except discord.HTTPException as e:
        if e.status == 429:
            print(
                "The Discord servers denied the connection for making too many requests"
            )
            print(
                "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
            )
        else:
            raise e
