import boto3

msg = input('Enter: ')

polly = boto3.client('polly')



result = polly.synthesize_speech(Text=msg, OutputFormat='mp3', VoiceId='Justin')
print(result)

# Save Audio
audio = result['AudioStream'].read()
print('==================================================')
print(type(audio))

with open('./MP3/myAudioFile.mp3', 'wb') as f:
    f.write(audio)