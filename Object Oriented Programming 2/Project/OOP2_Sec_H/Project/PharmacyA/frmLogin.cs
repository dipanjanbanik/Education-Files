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
    public partial class frmLogin : MetroFramework.Forms.MetroForm
    {
        static frmLogin _instance;

        public static frmLogin Instance
        {
            get
            {
                if (_instance == null)
                    _instance = new frmLogin();
                return _instance;
            }
        }
        public frmLogin()
        {
            InitializeComponent();
            MetroFramework.MetroMessageBox.Show(this, "\n--: Admin Login :--\nUser: admin            Password: admin123\n\n--: Salesman Login :--\nUser: salesman       Password: salesman123", "Login Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void frmLogin_Load(object sender, EventArgs e)
        {
            _instance = this;
            txtUserName.Focus();
        }

        private void btnLogin_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(txtUserName.Text) || string.IsNullOrEmpty(txtPassword.Text))
            {
                MetroFramework.MetroMessageBox.Show(this, "\n\nPlease enter both Username and Password", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                txtUserName.Focus();
                return;
            }

            try
            {
                using (PAEntities db = new PAEntities())
                {
                    var query = from u in db.User
                                where u.Uname == txtUserName.Text && u.Password == txtPassword.Text && u.Keyword == cmbxKeyword.Text
                                select u;

                    if (query.SingleOrDefault() != null)
                    {
                        this.Hide();
                        frmMain frm = new frmMain(string.Format("User: {0}", txtUserName.Text), cmbxKeyword.Text);
                        frm.ShowDialog();
                    }
                    else
                        MetroFramework.MetroMessageBox.Show(this, "Your Username or Password is incorrect", "Message", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MetroFramework.MetroMessageBox.Show(this, ex.Message, "Message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            txtPassword.Clear();
            txtUserName.Clear();
        }
    }
}
