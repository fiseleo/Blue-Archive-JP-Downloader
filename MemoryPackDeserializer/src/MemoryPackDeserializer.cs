using System;
using System.IO;
using MemoryPack;
using Newtonsoft.Json;

namespace MemoryPackDeserializer
{
    public enum MediaType
    {
        None = 0,
        Audio = 1,
        Video = 2,
        Texture = 3
    }

    [MemoryPackable]
    public partial class Media
    {
        public string Path { get; set; }
        public string FileName { get; set; }
        public long Bytes { get; set; }
        public long Crc { get; set; }
        public bool IsPrologue { get; set; }
        public bool IsSplitDownload { get; set; }
        public MediaType MediaType { get; set; }
    }

    [MemoryPackable]
    public partial class MediaCatalog
    {
        public Dictionary<string, Media> Table { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {

            string inputFilePath = args[0];
            string outputFilePath = args[1];

            byte[] catalogBytesFile = File.ReadAllBytes(inputFilePath);
            MediaCatalog mediaCatalog = MemoryPackSerializer.Deserialize<MediaCatalog>(catalogBytesFile);

            string json = JsonConvert.SerializeObject(mediaCatalog, Formatting.Indented);
            File.WriteAllText(outputFilePath, json);

            Console.WriteLine("Deserialization complete. JSON output written to " + outputFilePath);
        }
    }
}
