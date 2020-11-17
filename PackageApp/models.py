from PackageApp import db, admin
from sqlalchemy import Column, String, Integer, Boolean
from flask_login import UserMixin, current_user, logout_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask import redirect


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50), nullable=False)
    user_active = Column(Boolean, default=True)
    user_name = Column(String(50), nullable=False)
    user_password = Column(String(50), nullable=False)
    user_roles = Column(String(50), nullable=False)

    pass


# ---------------------------------------------------------------------------

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

# -------------------------- Phần ModelView --------------------------------------


class UserModelView(ModelView):
    # column_display_pk = True  # HIển thị khóa chính ra

    can_create = True
    can_edit = True
    can_export = True
    column_labels = dict(fullname="Tên người dùng", user_active="Kích hoạt", user_name="Tên đăng nhập",
                         user_password="Mật khẩu", user_roles="Vai trò người dùng")

    pass


# -----------------------------------


class AboutUsView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render("admin/about-us.html")

    def is_accessible(self):
        return current_user.is_authenticated

    pass


class LogoutAdminView(BaseView):
    @expose("/")
    def __index__(self):
        logout_user()
        return redirect("/admin")


# --------------------------------------------------------------------------------


admin.add_view(UserModelView(User, db.session, name="Quản lý người dùng"))


# ---------------------------------

admin.add_view(AboutUsView(name="Giới thiệu"))
admin.add_view(LogoutAdminView(name="Đăng xuất"))
# ham chay khoi tao database len mysql
if __name__ == "__main__":
    db.create_all()

