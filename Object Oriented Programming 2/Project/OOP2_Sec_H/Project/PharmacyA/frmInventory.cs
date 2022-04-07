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
    public partial class frmInventory : MetroFramework.Forms.MetroForm
    {
        public frmInventory()
        {
            InitializeComponent();
        }

        private void frmInventory_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'pAds.ProductInfo' table. You can move, or remove it, as needed.
            this.productInfoTableAdapter.Fill(this.pAds.ProductInfo);

        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            txtBoxNo.Clear();
            txtCName.Clear();
            txtName.Clear();
            txtQuantity.Clear();
            txtUnitPrice.Clear();
        }

        private void gridProductInfo_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = this.gridProductInfo.Rows[e.RowIndex];
                txtName.Text = row.Cells[1].Value.ToString();
                txtCName.Text = row.Cells[2].Value.ToString();
                txtBoxNo.Text = row.Cells[3].Value.ToString();
                txtQuantity.Text = row.Cells[4].Value.ToString();
                txtUnitPrice.Text = row.Cells[5].Value.ToString();
            }
        }

        private void txtUnitPrice_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(txtUnitPrice.Text, "  ^ [0-9]"))
            {
                txtUnitPrice.Text = "";
            }
        }

        private void txtUnitPrice_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }

        private void txtQuantity_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(txtQuantity.Text, "  ^ [0-9]"))
            {
                txtQuantity.Text = "";
            }
        }

        private void txtQuantity_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }
    }
}
