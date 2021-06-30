import boto3

msg = input('')

polly = boto3.client('polly')



result = polly.synthesize_speech(Text=msg, OutputFormat='mp3', VoiceId='Justin')

# Save Audio
audio = result['AudioStream'].read()

with open('helloworld.mp3', 'wb') as f:
    f.write(audio)