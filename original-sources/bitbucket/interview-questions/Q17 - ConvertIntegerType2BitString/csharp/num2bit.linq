<Query Kind="Program">
  <Output>DataGrids</Output>
</Query>

void Main()
{
	for (int i = -10; i <= 10; i++)
	{
		Console.WriteLine($"{i,6} ==> {Num2Bit1(i)}");
	}

	for (int i = -10; i <= 10; i++)
	{
		Console.WriteLine($"{i,6} ==> {Num2Bit2(i)}");
	}
}

// You can define other methods, fields, classes and namespaces here
public static string Num2Bit1(int n)
{
	if (n == 0)
	{
		return "0";
	}
	
	bool highbiton = false;
	if (n < 0)
	{
		highbiton = true;
		n &= 0x7FFFFFFF;
	}
	
	string bits = string.Empty;
	while (n != 0)
	{
		if ((n & 1) == 1)
		{
			bits = "1" + bits;
		}
		else
		{
			bits = "0" + bits;
		}
		
		n >>= 1;
	}
	
	if (highbiton)
	{
		bits = "1" + bits;
	}
	
	return bits;
}

public static string Num2Bit2(int n)
{
	int size = 32;
	char[] bits = new char[size];
	for (int k = 0; k < size; k++)
	{
		bits[k] = '0';
	}

	if (n == 0)
	{
		return new string(bits);
	}

	bool highbiton = false;
	if (n < 0)
	{
		highbiton = true;
		n &= 0x7FFFFFFF;
	}
	
	int i = 0;
	while (n != 0)
	{
		if ((n & 1) == 1)
		{
			bits[size - 1 -i] = '1';
		}

		n >>= 1;
		i++;
	}

	if (highbiton)
	{
		bits[0] = '1';
	}
	return new string(bits);

}