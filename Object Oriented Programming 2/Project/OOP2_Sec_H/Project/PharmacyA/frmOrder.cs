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
    public partial class frmOrder : MetroFramework.Forms.MetroForm
    {
        public frmOrder()
        {
            InitializeComponent();
        }

        private void frmOrder_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'nDS.Order' table. You can move, or remove it, as needed.
            //this.orderTableAdapter.Fill(this.nDS.Order);
            // TODO: This line of code loads data into the 'nDS.Order' table. You can move, or remove it, as needed.
            this.orderTableAdapter.Fill(this.nDS.Order);

        }

        private void gridOrder_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = this.gridOrder.Rows[e.RowIndex];
                txtName.Text = row.Cells[0].Value.ToString();
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            txtName.Clear();
            txtPrice.Clear();
            txtQuantity.Clear();
        }
    }
}
