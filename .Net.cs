[Route("api/[controller]")]
[ApiController]
public class HomeController : ControllerBase
{
    [HttpGet("getdata")]
    public IActionResult GetData()
    {
        return Ok("Hello from controller!");
    }
}

var result = List.FirstOrDefault(x => x.Id == 10);
var names = users.Select( u => u.Name).ToList();


public List<Product> GetAvailableProducts()
{
    var products = _dbContext.Products.ToList();
    var available = products.Where(p => p.IsAvailable).ToList();
    
    Log(available.Count + "products found.");
    
    return available;
}

public List<Product> GetAvailableProducts()
{
    return _dbContext.Products.Where(p => p.IsAvailable).ToList();
}

vr fisrtUser = users.FirstOrDefault(u => i.Id == 5);
Assert.NotNull(firstUser);


var result = list.ForstOrDefault(x => x.Id = 10);



FirstOrDefault()
Get the first item from the collection, or null/default if nothing found.
use when you expect one match or none.

var user = users.FirstOrDefault(u => u.Id == 10);

First()
Gets the first item, throws error if none found.
Use only when you're 100% sure at least one exists.

var user = users.First(u => u.Id == 10);


SingleOrDefault()
Returns a single matching item, or null if none, but throws if more than one found.
Use when expecting exactly one or none.

var user = users.SingleOrDefault(u => u.Email == "singh.santosh2702@gmail.com");

Single()
Returns exactly one item, throws if none or multiple found.
Use only if guaranteed only one match.

var admin = users.Single(u => u.Role == "Admin");


Where()
Filters and returns all matches as a list.
Use when you want multiple results.

var activeUsers = users.Where(u = > u.IsActive).ToList();


Any()
Checks if any item matches a condition - returns true/false.
Use for existence check.

bool hasAdmins = users.Any(u => u.Role == "Admin");

All()
Checks if all items satisfy a condition.
Use when verifying uniformity in data.

bool allActive = users.All(u => u.IsActive);


Select()
Transforms each item into something else (like DTO).
Use to project specific fields or map models.

var names = users.Selcet(u => u.Name).ToList();

SelectMany()
Flattens a list of lists into a single list.
Use for nested collections (e.g., user.Orders).

var allOrders = users.SelectMany(u => u.Orders).ToList();

OrderBy()/OrderByDescending()
Sorts the data ascending or descending.
Use to sort lists based on a property.

var sortedUsers = users.OrderBy(u => u.Name).ToList();
var highToLow = users.OrderByDescending(u => u.Age).ToList();

Take(n)/Skip(n)
Take(n) gets first N items. Skip(n) ignores first N items.
Use for pagination.

var page1 = users.skip(0).Take(10).ToList();
var page2 = users.Skip(10).Take(10).ToList();


Count()/Count(predicate)
Returns total number of items or number of matches.
Use to check how many items exist.

var total = users.Count();
var active = users.Count(u => u.IsActive);

Max()/Min()/Average()/Sum()
Performs aggregate math operations.
Use on numeric fields.

int maxAge = users.Max(u => u.Age);
double avgAge = users.Average(u => u.Age);
int sumAge = users.Sum(u => u.Age);


GroupBy()
Group items by a key (like Role or Department).
Use to create buckets or categorize data.

var grouped = users.GroupBy(u => u.Role);
foreach (var group in grouped)
{
    Console.WL(group.key);
    foreach (var user in group)
        C.WL(user.Name);
}


Distinct()/DistinctBy()
Removes duplicates.
Use to get unique values

var UniqueNames = users.Select(u => u.Name).Distinct().ToList();
// .Net 6+
var uniqueByEmail = users.DistinctBy( u => u.Email).ToList()


ToList()/ToArray()/ToDictionary()
Converts LINQ query results to real data structure.
Use to finalize the result.

var list = users.ToList();
var dict = users.ToDictionary(u => u.Id, u => u.Name);

DefaultIfEmpty()
Returns default value if collection is empty.
Use when you want to avoid null errors.

var safeList = users.DefaultIfEmpty().ToList();


var topAdmins = users.Where(u => u.Role == "Admin" && u.IsActive).OrderByDescending(u => u.CreatedAt)
    .Take(5)
    .Select(u => new{ u.Name, u.Email })
    .ToList();


























