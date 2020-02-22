import subprocess
import os

def mk_starts_ends (cdir, movie) :
    os.chdir(cdir)
    output = subprocess.run(["ffmpeg", "-i", movie, "-af", "silencedetect=noise=-20dB:d=0.2", "-f", "null", "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(output)
    s = str(output)
    lines = s.split('\\n')
    time_list = []
    for line in lines:
        if "silencedetect" in line:
            words = line.split(" ")
            for i in range(len(words)):
                if "silence_start" in words[i]:
                    start_time = words[i + 1]
                    time_list.append(float(start_time[:-2]))
                if "silence_end" in words[i]:
                    end_time = words[i + 1]
                    time_list.append(float(end_time[:-2]))
    print(time_list)
    return time_list
    #ありがとうございます
    


def exstract_voice (starts_ends, cdir):
    os.chdir(cdir)
    subprocess.run(["ffmpeg", "-i", movie, "-af", "silencedetect=noise=-33dB:d=0.6", "-f", "null", "-"])


if __name__ == '__main__':
    cdir = r"P:\video-stream-edit"
    movie = "Terracehouse.mp4"
    starts_ends = mk_starts_ends(cdir, movie)
    exstract_voice(starts_ends)