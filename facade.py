# Subsystem classes

class VideoFile:
    def __init__(self, filename):
        self.filename = filename

class Codec:
    def compress(self, video_file):
        pass

    def decompress(self, video_file):
        pass

class MPEG4CompressionCodec(Codec):
    def compress(self, video_file):
        print(f"Compressing video file '{video_file.filename}' using MPEG4 codec")

    def decompress(self, video_file):
        print(f"Decompressing video file '{video_file.filename}' using MPEG4 codec")

class OGGCompressionCodec(Codec):
    def compress(self, video_file):
        print(f"Compressing video file '{video_file.filename}' using OGG codec")

    def decompress(self, video_file):
        print(f"Decompressing video file '{video_file.filename}' using OGG codec")

# Facade
class VideoConverter:
    def __init__(self):
        self.codec = None

    def convert(self, filename, format):
        video_file = VideoFile(filename)
        if format == 'mp4':
            self.codec = MPEG4CompressionCodec()
        elif format == 'ogg':
            self.codec = OGGCompressionCodec()
        else:
            raise ValueError("Unsupported format")

        self.codec.compress(video_file)
        print(f"Converting video file '{filename}' to '{format}' format")
        self.codec.decompress(video_file)

# Client code
def main():
    converter = VideoConverter()
    converter.convert("video.avi", "mp4")

if __name__ == "__main__":
    main()