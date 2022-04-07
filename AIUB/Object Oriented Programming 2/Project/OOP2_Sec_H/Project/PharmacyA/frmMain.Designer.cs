namespace PharmacyA
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.mtabControl = new MetroFramework.Controls.MetroTabControl();
            this.mtabOption = new MetroFramework.Controls.MetroTabPage();
            this.titeTransaction = new MetroFramework.Controls.MetroTile();
            this.tileOrder = new MetroFramework.Controls.MetroTile();
            this.tileCart = new MetroFramework.Controls.MetroTile();
            this.tileEditInventory = new MetroFramework.Controls.MetroTile();
            this.tileAddUser = new MetroFramework.Controls.MetroTile();
            this.mtabSettings = new MetroFramework.Controls.MetroTabPage();
            this.rbLight = new MetroFramework.Controls.MetroRadioButton();
            this.rbDark = new MetroFramework.Controls.MetroRadioButton();
            this.metroLabel1 = new MetroFramework.Controls.MetroLabel();
            this.lblUserInfo = new MetroFramework.Controls.MetroLabel();
            this.linkExit = new MetroFramework.Controls.MetroLink();
            this.msmMain = new MetroFramework.Components.MetroStyleManager(this.components);
            this.metroLabel3 = new MetroFramework.Controls.MetroLabel();
            this.mtabControl.SuspendLayout();
            this.mtabOption.SuspendLayout();
            this.mtabSettings.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.msmMain)).BeginInit();
            this.SuspendLayout();
            // 
            // mtabControl
            // 
            this.mtabControl.Controls.Add(this.mtabOption);
            this.mtabControl.Controls.Add(this.mtabSettings);
            this.mtabControl.Location = new System.Drawing.Point(23, 114);
            this.mtabControl.Name = "mtabControl";
            this.mtabControl.SelectedIndex = 0;
            this.mtabControl.Size = new System.Drawing.Size(461, 279);
            this.mtabControl.TabIndex = 1;
            this.mtabControl.UseSelectable = true;
            // 
            // mtabOption
            // 
            this.mtabOption.BackColor = System.Drawing.SystemColors.Control;
            this.mtabOption.Controls.Add(this.titeTransaction);
            this.mtabOption.Controls.Add(this.tileOrder);
            this.mtabOption.Controls.Add(this.tileCart);
            this.mtabOption.Controls.Add(this.tileEditInventory);
            this.mtabOption.Controls.Add(this.tileAddUser);
            this.mtabOption.HorizontalScrollbarBarColor = true;
            this.mtabOption.HorizontalScrollbarHighlightOnWheel = false;
            this.mtabOption.HorizontalScrollbarSize = 10;
            this.mtabOption.Location = new System.Drawing.Point(4, 38);
            this.mtabOption.Name = "mtabOption";
            this.mtabOption.Size = new System.Drawing.Size(453, 237);
            this.mtabOption.TabIndex = 0;
            this.mtabOption.Text = "Option";
            this.mtabOption.VerticalScrollbarBarColor = true;
            this.mtabOption.VerticalScrollbarHighlightOnWheel = false;
            this.mtabOption.VerticalScrollbarSize = 10;
            // 
            // titeTransaction
            // 
            this.titeTransaction.ActiveControl = null;
            this.titeTransaction.Location = new System.Drawing.Point(275, 121);
            this.titeTransaction.Name = "titeTransaction";
            this.titeTransaction.Size = new System.Drawing.Size(116, 94);
            this.titeTransaction.TabIndex = 9;
            this.titeTransaction.Text = "Transaction";
            this.titeTransaction.UseSelectable = true;
            this.titeTransaction.Click += new System.EventHandler(this.titeTransaction_Click);
            // 
            // tileOrder
            // 
            this.tileOrder.ActiveControl = null;
            this.tileOrder.Location = new System.Drawing.Point(153, 121);
            this.tileOrder.Name = "tileOrder";
            this.tileOrder.Size = new System.Drawing.Size(116, 94);
            this.tileOrder.TabIndex = 8;
            this.tileOrder.Text = "Order Product";
            this.tileOrder.UseSelectable = true;
            this.tileOrder.Click += new System.EventHandler(this.tileOrder_Click);
            // 
            // tileCart
            // 
            this.tileCart.ActiveControl = null;
            this.tileCart.BackColor = System.Drawing.SystemColors.Control;
            this.tileCart.ForeColor = System.Drawing.SystemColors.ControlText;
            this.tileCart.Location = new System.Drawing.Point(31, 121);
            this.tileCart.Name = "tileCart";
            this.tileCart.Size = new System.Drawing.Size(116, 94);
            this.tileCart.TabIndex = 7;
            this.tileCart.Text = "View Cart";
            this.tileCart.UseSelectable = true;
            this.tileCart.Click += new System.EventHandler(this.tileCart_Click);
            // 
            // tileEditInventory
            // 
            this.tileEditInventory.ActiveControl = null;
            this.tileEditInventory.BackColor = System.Drawing.SystemColors.Control;
            this.tileEditInventory.Location = new System.Drawing.Point(31, 21);
            this.tileEditInventory.Name = "tileEditInventory";
            this.tileEditInventory.Size = new System.Drawing.Size(238, 94);
            this.tileEditInventory.TabIndex = 4;
            this.tileEditInventory.Text = "Inventory Information";
            this.tileEditInventory.TileImage = global::PharmacyA.Properties.Resources.Inventory;
            this.tileEditInventory.TileImageAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.tileEditInventory.UseSelectable = true;
            this.tileEditInventory.Click += new System.EventHandler(this.tileEditInventory_Click);
            // 
            // tileAddUser
            // 
            this.tileAddUser.ActiveControl = null;
            this.tileAddUser.Location = new System.Drawing.Point(275, 21);
            this.tileAddUser.Name = "tileAddUser";
            this.tileAddUser.Size = new System.Drawing.Size(116, 94);
            this.tileAddUser.TabIndex = 2;
            this.tileAddUser.Text = "Add User";
            this.tileAddUser.UseSelectable = true;
            this.tileAddUser.Click += new System.EventHandler(this.tileAddUser_Click);
            // 
            // mtabSettings
            // 
            this.mtabSettings.BackColor = System.Drawing.SystemColors.Control;
            this.mtabSettings.Controls.Add(this.rbLight);
            this.mtabSettings.Controls.Add(this.rbDark);
            this.mtabSettings.Controls.Add(this.metroLabel1);
            this.mtabSettings.ForeColor = System.Drawing.SystemColors.ControlText;
            this.mtabSettings.HorizontalScrollbarBarColor = true;
            this.mtabSettings.HorizontalScrollbarHighlightOnWheel = false;
            this.mtabSettings.HorizontalScrollbarSize = 10;
            this.mtabSettings.Location = new System.Drawing.Point(4, 38);
            this.mtabSettings.Name = "mtabSettings";
            this.mtabSettings.Size = new System.Drawing.Size(453, 237);
            this.mtabSettings.TabIndex = 1;
            this.mtabSettings.Text = "Settings";
            this.mtabSettings.VerticalScrollbarBarColor = true;
            this.mtabSettings.VerticalScrollbarHighlightOnWheel = false;
            this.mtabSettings.VerticalScrollbarSize = 10;
            // 
            // rbLight
            // 
            this.rbLight.AutoSize = true;
            this.rbLight.Location = new System.Drawing.Point(16, 60);
            this.rbLight.Name = "rbLight";
            this.rbLight.Size = new System.Drawing.Size(50, 15);
            this.rbLight.TabIndex = 5;
            this.rbLight.Text = "Light";
            this.rbLight.UseSelectable = true;
            this.rbLight.CheckedChanged += new System.EventHandler(this.rbLight_CheckedChanged);
            // 
            // rbDark
            // 
            this.rbDark.AutoSize = true;
            this.rbDark.Location = new System.Drawing.Point(16, 39);
            this.rbDark.Name = "rbDark";
            this.rbDark.Size = new System.Drawing.Size(47, 15);
            this.rbDark.TabIndex = 4;
            this.rbDark.Text = "Dark";
            this.rbDark.UseSelectable = true;
            this.rbDark.CheckedChanged += new System.EventHandler(this.rbDark_CheckedChanged);
            // 
            // metroLabel1
            // 
            this.metroLabel1.AutoSize = true;
            this.metroLabel1.Location = new System.Drawing.Point(3, 17);
            this.metroLabel1.Name = "metroLabel1";
            this.metroLabel1.Size = new System.Drawing.Size(49, 19);
            this.metroLabel1.TabIndex = 2;
            this.metroLabel1.Text = "Theme";
            // 
            // lblUserInfo
            // 
            this.lblUserInfo.AutoSize = true;
            this.lblUserInfo.Location = new System.Drawing.Point(302, 40);
            this.lblUserInfo.Name = "lblUserInfo";
            this.lblUserInfo.Size = new System.Drawing.Size(49, 19);
            this.lblUserInfo.TabIndex = 3;
            this.lblUserInfo.Text = "User: ?";
            // 
            // linkExit
            // 
            this.linkExit.BackColor = System.Drawing.SystemColors.Control;
            this.linkExit.Image = global::PharmacyA.Properties.Resources.Logout;
            this.linkExit.Location = new System.Drawing.Point(418, 29);
            this.linkExit.Name = "linkExit";
            this.linkExit.Size = new System.Drawing.Size(47, 30);
            this.linkExit.TabIndex = 4;
            this.linkExit.UseSelectable = true;
            this.linkExit.Click += new System.EventHandler(this.linkExit_Click);
            // 
            // msmMain
            // 
            this.msmMain.Owner = null;
            // 
            // metroLabel3
            // 
            this.metroLabel3.AutoSize = true;
            this.metroLabel3.Location = new System.Drawing.Point(418, 60);
            this.metroLabel3.Name = "metroLabel3";
            this.metroLabel3.Size = new System.Drawing.Size(53, 19);
            this.metroLabel3.TabIndex = 5;
            this.metroLabel3.Text = "LogOut";
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(507, 403);
            this.Controls.Add(this.metroLabel3);
            this.Controls.Add(this.linkExit);
            this.Controls.Add(this.lblUserInfo);
            this.Controls.Add(this.mtabControl);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "frmMain";
            this.Resizable = false;
            this.Text = "Dashboard";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.frmMain_FormClosed);
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.mtabControl.ResumeLayout(false);
            this.mtabOption.ResumeLayout(false);
            this.mtabSettings.ResumeLayout(false);
            this.mtabSettings.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.msmMain)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private MetroFramework.Controls.MetroTabControl mtabControl;
        private MetroFramework.Controls.MetroTabPage mtabOption;
        private MetroFramework.Controls.MetroTile tileOrder;
        private MetroFramework.Controls.MetroTile tileCart;
        private MetroFramework.Controls.MetroTile tileEditInventory;
        private MetroFramework.Controls.MetroTile tileAddUser;
        private MetroFramework.Controls.MetroTabPage mtabSettings;
        private MetroFramework.Controls.MetroLabel lblUserInfo;
        private MetroFramework.Controls.MetroRadioButton rbLight;
        private MetroFramework.Controls.MetroRadioButton rbDark;
        private MetroFramework.Controls.MetroLabel metroLabel1;
        private MetroFramework.Controls.MetroTile titeTransaction;
        private MetroFramework.Controls.MetroLink linkExit;
        private MetroFramework.Components.MetroStyleManager msmMain;
        private MetroFramework.Controls.MetroLabel metroLabel3;
    }
}