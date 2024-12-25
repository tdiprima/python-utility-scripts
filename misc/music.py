from music21 import stream, note, chord, midi

# Function to play a chord progression
def play_chord_progression(progression, key='C'):
    # Create a Stream to hold the notes
    s = stream.Stream()

    # Generate the chords based on the progression and key
    for p in progression:
        # Create a chord
        c = chord.Chord([key + str(p)])
        # Add the chord to the Stream
        s.append(c)

    # Play the Stream
    mf = midi.translate.streamToMidiFile(s)
    return mf

# I-IV-V chord progression in the key of C
progression = [1, 4, 5]
midi_file = play_chord_progression(progression)

# Saving the MIDI file to disk
file_path = '/Users/tdiprima/I_IV_V_Chord_Progression.mid'
midi_file.open(file_path, 'wb')
midi_file.write()
midi_file.close()

print(file_path)

