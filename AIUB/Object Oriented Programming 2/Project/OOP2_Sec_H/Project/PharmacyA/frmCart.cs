using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PharmacyA
{
    public partial class frmCart : MetroFramework.Forms.MetroForm
    {
        public frmCart()
        {
            InitializeComponent();
        }

        private void frmCart_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'nDS.CartInfo' table. You can move, or remove it, as needed.
            this.cartInfoTableAdapter.Fill(this.nDS.CartInfo);
            // TODO: This line of code loads data into the 'nDS.Order' table. You can move, or remove it, as needed.
            //this.orderTableAdapter.Fill(this.nDS.Order);

        }
    }
}
