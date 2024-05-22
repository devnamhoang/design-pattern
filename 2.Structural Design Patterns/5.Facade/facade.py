class File:
    pass


class VideoFile:
    pass


class OggCompressionCodec:
    pass


class MPEG4CompressionCodec:
    pass


class CodecFactory:
    pass


class BitrateReader:
    pass


class AudioMixer:
    pass


class VideoConverter:

    def convert(filename, format) -> File:
        file = VideoFile(filename)
        sourceCodec = CodecFactory().extract(file)
        if (format == "mp4"):
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = AudioMixer().fix(result)
        return File(result)


class Application:
    def main():
        convertor = VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()