# problem
song_line = input ("type the first line of your favourite song")

length_line = len(song_line)

print(f"the length of first line is {length_line}")

start = int(input("the starting index"))
end = int(input("the ending index"))

print(f" from {start} to end {end} is: {song_line[start:end]}")
