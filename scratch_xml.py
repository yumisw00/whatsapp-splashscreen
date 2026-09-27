import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

pkg_path = "app/src/main/java/com/whatsapp/splashscreen"
res_path = "app/src/main/res"

menu_xml = """<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/nav_home"
        android:title="Home" />
    <item
        android:id="@+id/nav_showcase"
        android:title="Showcase" />
    <item
        android:id="@+id/nav_form"
        android:title="Form" />
    <item
        android:id="@+id/nav_legacy"
        android:title="Legacy" />
</menu>
"""
write_file(f"{res_path}/menu/nav_menu.xml", menu_xml)

activity_main_xml = """<?xml version="1.0" encoding="utf-8"?>
<androidx.drawerlayout.widget.DrawerLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/drawer_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.coordinatorlayout.widget.CoordinatorLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <com.google.android.material.appbar.AppBarLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <androidx.appcompat.widget.Toolbar
                android:id="@+id/toolbar"
                android:layout_width="match_parent"
                android:layout_height="?attr/actionBarSize"
                android:background="?attr/colorPrimary"
                app:titleTextColor="@android:color/white" />
        </com.google.android.material.appbar.AppBarLayout>

        <androidx.fragment.app.FragmentContainerView
            android:id="@+id/fragment_container"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:layout_behavior="@string/appbar_scrolling_view_behavior"
            android:layout_marginBottom="56dp" />

        <com.google.android.material.bottomnavigation.BottomNavigationView
            android:id="@+id/bottom_nav"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_gravity="bottom"
            app:menu="@menu/nav_menu" />

    </androidx.coordinatorlayout.widget.CoordinatorLayout>

    <com.google.android.material.navigation.NavigationView
        android:id="@+id/nav_view"
        android:layout_width="wrap_content"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        app:menu="@menu/nav_menu" />

</androidx.drawerlayout.widget.DrawerLayout>
"""
write_file(f"{res_path}/layout/activity_main.xml", activity_main_xml)

fragment_home_xml = """<?xml version="1.0" encoding="utf-8"?>
<androidx.recyclerview.widget.RecyclerView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/recycler_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="8dp"
    android:clipToPadding="false" />
"""
write_file(f"{res_path}/layout/fragment_home.xml", fragment_home_xml)

item_layout_xml = """<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_margin="8dp"
    app:cardCornerRadius="8dp"
    app:cardElevation="4dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="16dp">

        <TextView
            android:id="@+id/tv_title"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textSize="18sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/tv_subtitle"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="4dp"
            android:textSize="14sp" />
    </LinearLayout>
</androidx.cardview.widget.CardView>
"""
write_file(f"{res_path}/layout/item_layout.xml", item_layout_xml)

fragment_showcase_xml = """<?xml version="1.0" encoding="utf-8"?>
<androidx.viewpager2.widget.ViewPager2 xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/view_pager"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
"""
write_file(f"{res_path}/layout/fragment_showcase.xml", fragment_showcase_xml)

fragment_showcase_page_xml = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:id="@+id/tv_page_content"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="24sp"
        android:textStyle="bold" />
</LinearLayout>
"""
write_file(f"{res_path}/layout/fragment_showcase_page.xml", fragment_showcase_page_xml)

fragment_form_xml = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Select an option:"
        android:layout_marginBottom="8dp"/>

    <Spinner
        android:id="@+id/spinner_options"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="16dp"/>

    <Button
        android:id="@+id/btn_show_dialog"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Show Dialog" />
        
    <Button
        android:id="@+id/btn_open_detail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:text="Open Detail Activity" />
</LinearLayout>
"""
write_file(f"{res_path}/layout/fragment_form.xml", fragment_form_xml)

fragment_legacy_list_xml = """<?xml version="1.0" encoding="utf-8"?>
<ListView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/list_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
"""
write_file(f"{res_path}/layout/fragment_legacy_list.xml", fragment_legacy_list_xml)

activity_detail_xml = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Detail Activity"
        android:textSize="24sp"
        android:layout_marginBottom="16dp"/>

    <Button
        android:id="@+id/btn_open_browser"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Open Browser (Implicit Intent)" />
</LinearLayout>
"""
write_file(f"{res_path}/layout/activity_detail.xml", activity_detail_xml)
