using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace testD.Datamodel
{
    public class Node
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        public string Name { get; set; }
        public string NubdChe { get; set; }
        public int? Parent_node_Id { get; set; }
        public string Vxod { get; set; }
        public string IzgPay { get; set; }
        public List<Ord> Ords { get; set; }
        public List<OrdsNode> OrdsNodes { get; set; }
    }

    public class PartsListModel
    {
        public int? Root { get; set; }
        public IEnumerable<Node> Nodes { get; set; }
    }
}
