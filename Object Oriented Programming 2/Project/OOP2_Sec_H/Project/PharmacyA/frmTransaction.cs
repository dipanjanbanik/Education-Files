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
    public partial class frmTransaction : MetroFramework.Forms.MetroForm
    {
        public frmTransaction()
        {
            InitializeComponent();
        }

        private void frmTransaction_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'nDS.Transaction' table. You can move, or remove it, as needed.
            this.transactionTableAdapter.Fill(this.nDS.Transaction);

        }
    }
}
