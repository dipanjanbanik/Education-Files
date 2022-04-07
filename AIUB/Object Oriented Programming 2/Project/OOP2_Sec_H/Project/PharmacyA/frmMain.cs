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
    public partial class frmMain : MetroFramework.Forms.MetroForm
    {
        bool _linkExit;
        string _keyword;
        public frmMain(string userinfo, string key)
        {
            InitializeComponent();
            lblUserInfo.Text = userinfo;
            _keyword = key;
            if (_keyword == "Salesman")
                tileAddUser.Enabled = false;
            this.StyleManager = msmMain;
        }

        private void linkExit_Click(object sender, EventArgs e)
        {
            _linkExit = true;
            this.Close();
            frmLogin.Instance.Show();
        }


        private void frmMain_FormClosed(object sender, FormClosedEventArgs e)
        {
            //main from close
            if (!_linkExit)
                Application.Exit();
        }


        private void frmMain_Load(object sender, EventArgs e)
        {
            
        }

        private void tileAddUser_Click(object sender, EventArgs e)
        {
            this.Hide();
            frmAddUser frm = new frmAddUser();
            frm.ShowDialog();
            this.Show();
        }

        private void tileEditInventory_Click(object sender, EventArgs e)
        {
            this.Hide();
            frmInventory frm = new frmInventory();
            frm.ShowDialog();
            this.Show();
        }

        private void tileOrder_Click(object sender, EventArgs e)
        {
            this.Hide();
            frmOrder frm = new frmOrder();
            frm.ShowDialog();
            this.Show();
        }

        private void tileCart_Click(object sender, EventArgs e)
        {
            this.Hide();
            frmCart frm = new frmCart();
            frm.ShowDialog();
            this.Show();
        }

        private void titeTransaction_Click(object sender, EventArgs e)
        {
            this.Hide();
            frmTransaction frm = new frmTransaction();
            frm.ShowDialog();
            this.Show();
        }

        private void rbDark_CheckedChanged(object sender, EventArgs e)
        {
            msmMain.Theme = MetroFramework.MetroThemeStyle.Dark;
        }

        private void rbLight_CheckedChanged(object sender, EventArgs e)
        {
            msmMain.Theme = MetroFramework.MetroThemeStyle.Light;
        }
    }
}
