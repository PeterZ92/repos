using MySql.Data.EntityFramework;
using System;
using System.Data.Common;
using System.Data.Entity;
using System.Linq;

namespace testD.Datamodel
{
    [DbConfigurationType(typeof(MySqlEFConfiguration))]
    public class sklad : DbContext
    {
        public DbSet<Ord> Ords { get; set; }
        public DbSet<Node> Nodes { get; set; }
        


        public sklad()
            : base(/*"name=sklad"*/)
        {
        }
        public sklad (DbConnection existingConnection, bool contextOwnsConnection)
             : base(existingConnection, contextOwnsConnection)
        {
           
        }
        // Добавьте DbSet для каждого типа сущности, который требуется включить в модель. Дополнительные сведения 

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Entity<OrdsNode>().
                 Property(o => o.NodeId).HasColumnOrder(0).HasColumnName("NodeId");
            modelBuilder.Entity<OrdsNode>().
                Property(o => o.OrdId).HasColumnOrder(1);
        }
    }

   
}