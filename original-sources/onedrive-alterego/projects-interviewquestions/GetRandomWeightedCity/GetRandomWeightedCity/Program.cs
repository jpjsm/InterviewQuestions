using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GetRandomWeightedCity
{
    public class City
    {
        public string Name { get; set; }
        public int Population { get; set; }
    }
    class Program
    {
        private static Random rnd = new Random();
        private static Dictionary<int, int> frequencies = new Dictionary<int, int>();
        static void Main(string[] args)
        {
            List<City> cities = new List<City>()
            {
                new City(){ Name = "Everett", Population=850},
                new City(){ Name = "Seattle", Population=2150},
                new City(){ Name = "Tacoma", Population=650},
                new City(){ Name = "Olympia", Population=350}
            };

            Dictionary<string, int> observations = new Dictionary<string, int>();
            Tuple<int, string>[] rankedCities = new Tuple<int, string>[cities.Count];
            int totalPopulation = 0;
            int index = 0;
            foreach (var city in cities.OrderByDescending(c => c.Population))
            {
                totalPopulation += city.Population;
                rankedCities[index++] = new Tuple<int, string>(totalPopulation, city.Name);
                observations.Add(city.Name, 0);
            }

            for (int i = 0; i < 10000; i++)
            {
                observations[GetRandomWeightedCity(rankedCities)]++;
            }

            foreach (var key in frequencies.Keys.OrderBy(k => k))
            {
                Console.WriteLine("Bucket: {0,5:N0} {1,5:N0}", key, frequencies[key]);
            }

            foreach (var city in cities.OrderByDescending(c => c.Population))
            {
                Console.WriteLine(
                    "{0,-10} {1,5:N0} {2,9:N3} {3,9:N3}", 
                    city.Name, 
                    city.Population, 
                    ((double)city.Population)/totalPopulation, 
                    ((double)observations[city.Name])/10000);
            }
        }

        public static string GetRandomWeightedCity(Tuple<int, string>[] rankedCities)
        {
            if (rankedCities == null || rankedCities.Length == 0)
            {
                throw new ArgumentNullException("rankedCities");
            }

            if(rankedCities.Length == 1)
            {
                return rankedCities[0].Item2;
            }

            int weightedIndex = (int)(rankedCities[rankedCities.Length - 1].Item1 * rnd.NextDouble());
            int weightedIndexRange = (weightedIndex / 100) * 100;
            if (frequencies.ContainsKey(weightedIndexRange))
            {
                frequencies[weightedIndexRange]++;
            }
            else
            {
                frequencies.Add(weightedIndexRange, 1);
            }

            for (int i = 0; i < rankedCities.Length ; i++)
            {
                if(weightedIndex < rankedCities[i].Item1)
                {
                    return rankedCities[i].Item2;
                }
            }

            return rankedCities[rankedCities.Length - 1].Item2;
        }
    }
}
