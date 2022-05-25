using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace testD.Datamodel
{
    public class OrdsNode
    {  
        public int NodeId { get; set; }
        public Node Node { get; set; }

       

        public int OrdId { get; set; }
        public Ord Ord { get; set; }

        public int FactQua { get; set; }
        public int Potreb { get; set; }

        //public int Deficite { get; set; } // дефицит возможно считается
        public int NaSborky { get; set; }
    }
}
