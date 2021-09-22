using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace WebAPI.Controllers
{
    public class DefaultController : ApiController
    {
        // GET
        public IEnumerable<string> Get()
        {
            //return Ok<Dictionary<string, object>>(null);
            return new string[] { "Connect sucsecc"};
        }
    }
}
