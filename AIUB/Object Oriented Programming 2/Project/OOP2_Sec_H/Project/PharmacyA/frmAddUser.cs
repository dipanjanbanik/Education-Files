using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace PharmacyA
{
    public partial class frmAddUser : MetroFramework.Forms.MetroForm
    {
        public frmAddUser()
        {
            InitializeComponent();
        }

        private void frmAddUser_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'pAds.UserandUserInfo' table. You can move, or remove it, as needed.
            this.userandUserInfoTableAdapter.Fill(this.pAds.UserandUserInfo);
        }

        private void frmAddUser_FormClosed(object sender, FormClosedEventArgs e)
        {
            this.Close();
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            txtFirstName.Clear();
            txtLastName.Clear();
            txtAddress.Clear();
            txtPhoneNo.Clear();
            txtUname.Clear();
            txtPassword.Clear();
            
        }

        private void btnSubmit_Click(object sender, EventArgs e)
        {
            try
            {
                using (PAEntities db = new PAEntities())
                {
                    //List<UserInfo> _userinformation = db.UserInfo.ToList<UserInfo>();
                    UserInfo _userinfo = new UserInfo();
                    _userinfo.FirstName = txtFirstName.Text;
                    _userinfo.LastName = txtLastName.Text;
                    _userinfo.Address = txtAddress.Text;
                    _userinfo.ContactNo = Convert.ToInt32(txtPhoneNo.Text);
                    //_userinfo.JoinDate = dtJoinDate.Value.Date;
                    db.Entry(_userinfo).State = System.Data.Entity.EntityState.Added;
                    db.SaveChanges();

                    User _user = new User();
                    _user.Uname = txtUname.Text;
                    _user.Password = txtPassword.Text;
                    _user.Keyword = cmbxKeyword.Text;
                    db.User.Add(_user);
                    db.SaveChanges();
                    

                }
            }
            catch (Exception ex)
            {
                MetroFramework.MetroMessageBox.Show(this, ex.Message, "Message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void txtPhoneNo_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(txtPhoneNo.Text, "  ^ [0-9]"))
            {
                txtPhoneNo.Text = "";
            }
        }

        private void txtPhoneNo_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }

        private void gridUserInformation_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = this.gridUserInformation.Rows[e.RowIndex];
                txtUname.Text = row.Cells[1].Value.ToString();
                txtPassword.Text = row.Cells[2].Value.ToString();
                cmbxKeyword.Text = row.Cells[3].Value.ToString();
                txtFirstName.Text = row.Cells[4].Value.ToString();
                txtLastName.Text = row.Cells[5].Value.ToString();
                txtAddress.Text = row.Cells[6].Value.ToString();
                txtPhoneNo.Text = row.Cells[7].Value.ToString();
            }
        }
    }
}
