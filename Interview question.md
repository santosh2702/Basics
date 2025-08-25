# Interview Questions (from 3 interviews)


## Core C# / .NET

* Difference between **string** and **StringBuilder**
* **Delegate**
* **Event**
* Explain **abstraction**
* Difference between **const** and **readonly**
* What is the difference between **ref** and **val**
* Difference between **double** and **Int32**

## Coding / Logic (C#)

* Reverse a string (give logic)
* What will be the output of code without curly braces in C#, but with `Console.WriteLine` inside a `while` loop where `i = 1` initially and condition is `i <= 5`

## Coding / Logic (Python)

* Find the **second largest** number of a list in Python

## String Manipulation (Mixed)

* Reverse a string that contains **numbers and letters**; **reverse only the letter part** and **keep numbers in place**

ANSWER

1) Difference between string and StringBuilder

string: Immutable. Any change creates a new string → extra allocations. Good for small/rare concatenations.

StringBuilder: Mutable buffer for repeated appends/inserts → efficient in loops.

// string (creates many temporaries in a loop)
var s = "";
for (int i = 0; i < 1000; i++) s += i;  // inefficient

// StringBuilder (preferred for many appends)
var sb = new System.Text.StringBuilder();
for (int i = 0; i < 1000; i++) sb.Append(i);
string result = sb.ToString();

2) Delegate (what & why)

A type-safe function pointer—a type that represents methods with a specific signature. Enables callbacks/multicast.

public delegate int Op(int x, int y);

static int Add(int a, int b) => a + b;

Op op = Add;           // point to method
int ans = op(2, 3);    // invoke

// Built-ins: Action (void), Func<TResult>, Predicate<T>
Func<int,int,int> add2 = (a,b) => a+b;

3) Event (what & why)

Publish/subscribe wrapper around a delegate. Only the declaring class can raise it; others can subscribe/unsubscribe.

public class Notifier
{
    public event EventHandler? Tick;
    public void Fire() => Tick?.Invoke(this, EventArgs.Empty);
}

var n = new Notifier();
n.Tick += (s,e) => Console.WriteLine("Tick!");
n.Fire(); // prints "Tick!"

4) Reverse a string (C# – logic + code)

Use two pointers and swap.

static string Reverse(string s)
{
    var arr = s.ToCharArray();
    int i = 0, j = arr.Length - 1;
    while (i < j) { (arr[i], arr[j]) = (arr[j], arr[i]); i++; j--; }
    return new string(arr);
}
// Quick one-liner: new string(s.Reverse().ToArray())

5) Reverse only letters; keep digits in place

Idea: two pointers; skip digits; swap letters only.

C#

static string ReverseLettersKeepDigits(string s)
{
    var a = s.ToCharArray();
    int i = 0, j = a.Length - 1;

    bool IsLetter(char c) => char.IsLetter(c);

    while (i < j)
    {
        if (!IsLetter(a[i])) { i++; continue; }
        if (!IsLetter(a[j])) { j--; continue; }
        (a[i], a[j]) = (a[j], a[i]); i++; j--;
    }
    return new string(a);
}
// "a1b2c3d" -> "d1c2b3a"


Python (same logic)

def reverse_letters_keep_digits(s: str) -> str:
    a = list(s)
    i, j = 0, len(a) - 1
    while i < j:
        if not a[i].isalpha():
            i += 1
        elif not a[j].isalpha():
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1; j -= 1
    return "".join(a)

6) Find the second largest number in a Python list

Handle duplicates; return None if it doesn’t exist.

def second_largest(nums):
    first = second = None
    for x in nums:
        if first is None or x > first:
            if first != x:  # move current first down
                second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second

# Examples:
# [3, 5, 1, 5, 4] -> 4
# [10] -> None
# [7,7,7] -> None

7) Explain abstraction

What: Show only what an object can do, hide how it does it.

How in C#: interface (pure contract) and abstract class (base with partial implementation).

public interface IPayment { void Pay(decimal amount); }
public class UpiPayment : IPayment { public void Pay(decimal amt) { /* hidden details */ } }


Benefits: simpler APIs, encapsulation, easier testing/substitution.

8) Difference between const and readonly

const

Compile-time constant; implicitly static.

Only primitive numbers, char, bool, string, and enum (and combinations).

Value baked into callers at compile time.

readonly

Runtime constant; can assign once in declaration or in constructor.

Can be any type (incl. objects, structs).

Different instances can hold different readonly values.

public class C {
    public const int Buffer = 4096;                // compile-time
    public readonly DateTime CreatedAt;            // runtime
    public C() { CreatedAt = DateTime.UtcNow; }    // set in ctor
}

9) While loop without braces (C#) – what’s the output?

If code is like:

int i = 1;
while (i <= 5)
    Console.WriteLine(i);


Only the very next statement is the loop body. There’s no increment → infinite loop printing 1 forever.
(Fix by adding braces and incrementing i.)

10) Reverse a string using C# (logic recap)

Convert to char[], swap with two pointers, or use Array.Reverse.

static string Reverse2(string s)
{
    var arr = s.ToCharArray();
    Array.Reverse(arr);
    return new string(arr);
}

11) Difference between ref and “val”

In C# there is no val keyword. You likely mean pass-by-reference (ref) vs pass-by-value (default).

Pass-by-value (default): method gets a copy of the value (for structs) or a copy of the reference (for classes). Reassigning the parameter doesn’t affect the caller’s variable.

ref: pass by reference; method can modify the caller’s variable itself (reassignment or in-place for structs).

Related: out (must assign inside) and in (read-only by ref).

static void IncByValue(int x) { x++; }            // caller unaffected
static void IncByRef(ref int x) { x++; }          // caller changes

int a = 1; IncByValue(a); // a == 1
int b = 1; IncByRef(ref b); // b == 2

12) Difference between double and Int32

Type: double = 64-bit IEEE 754 floating-point (fractional), Int32 = 32-bit signed integer.

Range/precision: double ~ ±1.7e308 with ~15–17 digits precision (not exact for many decimals). Int32 −2,147,483,648 to 2,147,483,647 (exact).

Use: double for measurements/continuous values; Int32 for counts/indices.

double d = 1.5;   // ok
int n = 1.5;      // compile error (needs cast); int holds whole numbers only
