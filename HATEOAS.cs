// In an OrdersController
[HttpGet("{id}")]
public IActionResult Get(string id, [FromServices] IUrlHelperFactory factory)
{
    var order = _repo.Find(id);
    if (order is null) return NotFound();

    var url = factory.GetUrlHelper(ControllerContext);

    var resource = new {
        id = order.Id,
        status = order.Status,
        _links = new Dictionary<string, object> {
            ["self"] = new { href = url.Link(null, new { controller = "Orders", action = nameof(Get), id }) }
        }
    };

    // add state-conditional links
    var links = (Dictionary<string, object>)resource._links;
    if (order.Status == "created")
    {
        links["pay"]    = new { href = url.Action(nameof(Pay),   "Orders", new { id }), method = "POST" };
        links["cancel"] = new { href = url.Action(nameof(Cancel),"Orders", new { id }), method = "POST" };
    }
    if (order.Status == "paid")
    {
        links["refund"] = new { href = url.Action(nameof(Refund),"Orders", new { id }), method = "POST" };
    }

    return Ok(resource);
}
