using System;

namespace ConsoleApp1
{
    public class Program
    {
        static string[] ids = {
            "Tokyo Standard Time",
            "Eastern Standard Time"
        };
        
        public static void Main(string[] args)
        {
            foreach(string id in ids)
            {
                DateTime date =
                    TimeZoneInfo.ConvertTimeFromUtc(DateTime.UtcNow, GetTimeZone(id));
                Console.WriteLine($"TimeZone:{id}");
                Console.WriteLine($"date:{date}");
            }
        }

        static TimeZoneInfo GetTimeZone(string id)
        {
            return TimeZoneInfo.FindSystemTimeZoneById(id);
        }
    }
}
