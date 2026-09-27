import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

# 1. Update Gradle Build File
build_gradle = """
plugins {
    alias(libs.plugins.android.application)
}

android {
    namespace = "com.showcase.allinone"
    compileSdk = 37

    defaultConfig {
        applicationId = "com.showcase.allinone"
        minSdk = 24
        targetSdk = 37
        versionCode = 1
        versionName = "1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    buildFeatures {
        viewBinding = true
    }
}

dependencies {
    implementation(libs.androidx.activity.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.androidx.constraintlayout)
    implementation(libs.androidx.core.ktx)
    implementation(libs.material)
    implementation("androidx.core:core-splashscreen:1.0.1")
    implementation("androidx.recyclerview:recyclerview:1.3.2")
    implementation("androidx.viewpager2:viewpager2:1.1.0")
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(libs.androidx.junit)
}
"""
write_file("app/build.gradle.kts", build_gradle)

# 2. Android Manifest
manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.App.SplashScreen">
        <activity
            android:name=".MainActivity"
            android:theme="@style/Theme.App.SplashScreen"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity
            android:name=".SecondActivity"
            android:theme="@style/Theme.AllInOne"
            android:exported="false" />
    </application>
</manifest>
"""
write_file("app/src/main/AndroidManifest.xml", manifest)

# 3. Resources: colors, strings, themes
colors_xml = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="purple_200">#FFBB86FC</color>
    <color name="purple_500">#FF6200EE</color>
    <color name="purple_700">#FF3700B3</color>
    <color name="teal_200">#FF03DAC5</color>
    <color name="teal_700">#FF018786</color>
    <color name="black">#FF000000</color>
    <color name="white">#FFFFFFFF</color>
    <color name="splash_bg">#FF6200EE</color>
    <color name="yellow_active">#FFFFEB3B</color>
</resources>
"""
write_file("app/src/main/res/values/colors.xml", colors_xml)

strings_xml = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">All In One</string>
    <string name="open_drawer">Open Drawer</string>
    <string name="close_drawer">Close Drawer</string>
</resources>
"""
write_file("app/src/main/res/values/strings.xml", strings_xml)

themes_xml = """<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Base.Theme.AllInOne" parent="Theme.Material3.DayNight.NoActionBar">
        <item name="colorPrimary">@color/purple_500</item>
        <item name="colorPrimaryVariant">@color/purple_700</item>
        <item name="colorOnPrimary">@color/white</item>
        <item name="colorSecondary">@color/teal_200</item>
        <item name="colorSecondaryVariant">@color/teal_700</item>
        <item name="colorOnSecondary">@color/black</item>
    </style>
    <style name="Theme.AllInOne" parent="Base.Theme.AllInOne" />
    <style name="Theme.App.SplashScreen" parent="Theme.SplashScreen">
        <item name="windowSplashScreenBackground">@color/splash_bg</item>
        <!-- For real app, point to a drawable logo. Using default app icon for this setup -->
        <item name="windowSplashScreenAnimatedIcon">@mipmap/ic_launcher</item>
        <item name="postSplashScreenTheme">@style/Theme.AllInOne</item>
    </style>
</resources>
"""
write_file("app/src/main/res/values/themes.xml", themes_xml)

# 4. Menus
nav_drawer_menu = """<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/nav_home" android:title="Home" />
    <item android:id="@+id/nav_settings" android:title="Settings" />
    <item android:id="@+id/nav_share" android:title="Share" />
    <item android:id="@+id/nav_about" android:title="About" />
    <item android:id="@+id/nav_logout" android:title="Logout" />
</menu>
"""
write_file("app/src/main/res/menu/nav_drawer_menu.xml", nav_drawer_menu)

bottom_nav_menu = """<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/bottom_home" android:title="Home" android:icon="@android:drawable/ic_menu_compass" />
    <item android:id="@+id/bottom_search" android:title="Search" android:icon="@android:drawable/ic_menu_search" />
    <item android:id="@+id/bottom_add" android:title="Add" android:icon="@android:drawable/ic_menu_add" />
    <item android:id="@+id/bottom_reels" android:title="Reels" android:icon="@android:drawable/ic_menu_gallery" />
    <item android:id="@+id/bottom_profile" android:title="Profile" android:icon="@android:drawable/ic_menu_myplaces" />
</menu>
"""
write_file("app/src/main/res/menu/bottom_nav_menu.xml", bottom_nav_menu)

# 5. Layouts
activity_main = """<?xml version="1.0" encoding="utf-8"?>
<androidx.drawerlayout.widget.DrawerLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/drawer_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true">

    <androidx.coordinatorlayout.widget.CoordinatorLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <com.google.android.material.appbar.AppBarLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content">
            <com.google.android.material.appbar.MaterialToolbar
                android:id="@+id/top_toolbar"
                android:layout_width="match_parent"
                android:layout_height="?attr/actionBarSize"
                android:background="?attr/colorPrimary"
                app:titleTextColor="@android:color/white"/>
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
            app:menu="@menu/bottom_nav_menu"
            app:itemActiveIndicatorStyle="@style/CustomBottomNavIndicator" />

    </androidx.coordinatorlayout.widget.CoordinatorLayout>

    <com.google.android.material.navigation.NavigationView
        android:id="@+id/nav_view"
        android:layout_width="wrap_content"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        app:headerLayout="@layout/nav_header"
        app:menu="@menu/nav_drawer_menu" />

</androidx.drawerlayout.widget.DrawerLayout>
"""
write_file("app/src/main/res/layout/activity_main.xml", activity_main)

# Missing style for custom bottom nav indicator: append to themes.xml
themes_xml_append = """
    <style name="CustomBottomNavIndicator">
        <item name="android:tint">@color/yellow_active</item>
    </style>
</resources>
"""
# Since I wrote themes.xml above, I will just rewrite themes.xml completely.
themes_xml = themes_xml.replace("</resources>", themes_xml_append)
write_file("app/src/main/res/values/themes.xml", themes_xml)

nav_header = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="176dp"
    android:background="@color/purple_500"
    android:gravity="bottom"
    android:orientation="vertical"
    android:padding="16dp"
    android:theme="@style/ThemeOverlay.AppCompat.Dark">

    <ImageView
        android:layout_width="64dp"
        android:layout_height="64dp"
        android:src="@mipmap/ic_launcher_round" />
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp"
        android:text="User Name"
        android:textAppearance="@style/TextAppearance.AppCompat.Body1"
        android:textStyle="bold" />
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="user@example.com" />
</LinearLayout>
"""
write_file("app/src/main/res/layout/nav_header.xml", nav_header)

activity_second = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="16dp">
    <TextView
        android:id="@+id/tv_payload"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="20sp"
        android:layout_marginBottom="16dp"/>
    <Button
        android:id="@+id/btn_back"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Back (Finish)"
        android:layout_marginBottom="16dp"/>
    <Button
        android:id="@+id/btn_implicit_intent"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Open Browser (Implicit Intent)" />
</LinearLayout>
"""
write_file("app/src/main/res/layout/activity_second.xml", activity_second)

item_card = """<?xml version="1.0" encoding="utf-8"?>
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
        android:orientation="horizontal"
        android:padding="16dp"
        android:gravity="center_vertical">
        <ImageView
            android:id="@+id/img_icon"
            android:layout_width="60dp"
            android:layout_height="60dp"
            android:src="@mipmap/ic_launcher" />
        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_marginStart="16dp"
            android:orientation="vertical">
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
    </LinearLayout>
</androidx.cardview.widget.CardView>
"""
write_file("app/src/main/res/layout/item_card.xml", item_card)

page_layout = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">
    <TextView
        android:id="@+id/tv_page"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="32sp"
        android:textStyle="bold" />
</LinearLayout>
"""
write_file("app/src/main/res/layout/page_layout.xml", page_layout)

fragment_home = """<?xml version="1.0" encoding="utf-8"?>
<androidx.recyclerview.widget.RecyclerView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/recycler_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:clipToPadding="false"
    android:padding="8dp" />
"""
write_file("app/src/main/res/layout/fragment_home.xml", fragment_home)

fragment_pager = """<?xml version="1.0" encoding="utf-8"?>
<androidx.viewpager2.widget.ViewPager2 xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/view_pager"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
"""
write_file("app/src/main/res/layout/fragment_pager.xml", fragment_pager)

fragment_form = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    android:gravity="center">
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Choose Ice Cream Flavor:"
        android:layout_marginBottom="8dp"/>
    <Spinner
        android:id="@+id/spinner_flavor"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="24dp"/>
    <Button
        android:id="@+id/btn_alert"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Show Alert Dialog" />
</LinearLayout>
"""
write_file("app/src/main/res/layout/fragment_form.xml", fragment_form)

fragment_legacy_list = """<?xml version="1.0" encoding="utf-8"?>
<ListView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/list_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
"""
write_file("app/src/main/res/layout/fragment_legacy_list.xml", fragment_legacy_list)

# KOTLIN FILES
pkg = "com.showcase.allinone"
base = "app/src/main/java/com/showcase/allinone"

main_activity = f"""package {pkg}

import android.os.Bundle
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.core.view.GravityCompat
import androidx.fragment.app.Fragment
import {pkg}.databinding.ActivityMainBinding
import {pkg}.ui.FormFragment
import {pkg}.ui.HomeFragment
import {pkg}.ui.LegacyListFragment
import {pkg}.ui.ShowcasePagerFragment

class MainActivity : AppCompatActivity() {{
    private lateinit var binding: ActivityMainBinding
    private lateinit var toggle: ActionBarDrawerToggle

    override fun onCreate(savedInstanceState: Bundle?) {{
        installSplashScreen()
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.topToolbar)

        toggle = ActionBarDrawerToggle(
            this, binding.drawerLayout, binding.topToolbar,
            R.string.open_drawer, R.string.close_drawer
        )
        binding.drawerLayout.addDrawerListener(toggle)
        toggle.syncState()

        binding.navView.setNavigationItemSelectedListener {{ item ->
            when (item.itemId) {{
                R.id.nav_home -> binding.bottomNav.selectedItemId = R.id.bottom_home
                R.id.nav_settings -> Toast.makeText(this, "Settings clicked", Toast.LENGTH_SHORT).show()
                R.id.nav_share -> Toast.makeText(this, "Share clicked", Toast.LENGTH_SHORT).show()
                R.id.nav_about -> Toast.makeText(this, "About clicked", Toast.LENGTH_SHORT).show()
                R.id.nav_logout -> Toast.makeText(this, "Logout clicked", Toast.LENGTH_SHORT).show()
            }}
            binding.drawerLayout.closeDrawer(GravityCompat.START)
            true
        }}

        binding.bottomNav.setOnItemSelectedListener {{ item ->
            when (item.itemId) {{
                R.id.bottom_home -> replaceFragment(HomeFragment())
                R.id.bottom_search -> replaceFragment(ShowcasePagerFragment())
                R.id.bottom_add -> {{
                    Toast.makeText(this, "upload image and video", Toast.LENGTH_SHORT).show()
                    return@setOnItemSelectedListener false
                }}
                R.id.bottom_reels -> replaceFragment(FormFragment())
                R.id.bottom_profile -> replaceFragment(LegacyListFragment())
            }}
            true
        }}

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {{
            override fun handleOnBackPressed() {{
                if (binding.drawerLayout.isDrawerOpen(GravityCompat.START)) {{
                    binding.drawerLayout.closeDrawer(GravityCompat.START)
                }} else {{
                    isEnabled = false
                    onBackPressedDispatcher.onBackPressed()
                }}
            }}
        }})

        if (savedInstanceState == null) {{
            binding.bottomNav.selectedItemId = R.id.bottom_home
        }}
    }}

    private fun replaceFragment(fragment: Fragment) {{
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragment_container, fragment)
            .commit()
    }}
}}
"""
write_file(f"{base}/MainActivity.kt", main_activity)

second_activity = f"""package {pkg}

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import {pkg}.databinding.ActivitySecondBinding

class SecondActivity : AppCompatActivity() {{
    private lateinit var binding: ActivitySecondBinding

    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        binding = ActivitySecondBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val title = intent.getStringExtra("EXTRA_TITLE")
        binding.tvPayload.text = "Payload received:\\n$title"

        binding.btnBack.setOnClickListener {{
            finish()
        }}

        binding.btnImplicitIntent.setOnClickListener {{
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.google.com"))
            startActivity(intent)
        }}
    }}
}}
"""
write_file(f"{base}/SecondActivity.kt", second_activity)

model_item = f"""package {pkg}.model

data class ItemModel(val title: String, val subtitle: String)
"""
write_file(f"{base}/model/ItemModel.kt", model_item)

adapter_recycler = f"""package {pkg}.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import {pkg}.databinding.ItemCardBinding
import {pkg}.model.ItemModel

class RecyclerAdapter(
    private val items: List<ItemModel>,
    private val onItemClick: (ItemModel) -> Unit
) : RecyclerView.Adapter<RecyclerAdapter.ViewHolder>() {{

    inner class ViewHolder(val binding: ItemCardBinding) : RecyclerView.ViewHolder(binding.root) {{
        fun bind(item: ItemModel) {{
            binding.tvTitle.text = item.title
            binding.tvSubtitle.text = item.subtitle
            binding.root.setOnClickListener {{ onItemClick(item) }}
        }}
    }}

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {{
        val binding = ItemCardBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }}

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {{
        holder.bind(items[position])
    }}

    override fun getItemCount() = items.size
}}
"""
write_file(f"{base}/adapter/RecyclerAdapter.kt", adapter_recycler)

adapter_pager = f"""package {pkg}.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import {pkg}.databinding.PageLayoutBinding

class ViewPagerAdapter(private val pages: List<String>) : RecyclerView.Adapter<ViewPagerAdapter.PagerViewHolder>() {{

    inner class PagerViewHolder(val binding: PageLayoutBinding) : RecyclerView.ViewHolder(binding.root) {{
        fun bind(text: String) {{
            binding.tvPage.text = text
        }}
    }}

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PagerViewHolder {{
        val binding = PageLayoutBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return PagerViewHolder(binding)
    }}

    override fun onBindViewHolder(holder: PagerViewHolder, position: Int) {{
        holder.bind(pages[position])
    }}

    override fun getItemCount() = pages.size
}}
"""
write_file(f"{base}/adapter/ViewPagerAdapter.kt", adapter_pager)

home_fragment = f"""package {pkg}.ui

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import {pkg}.SecondActivity
import {pkg}.adapter.RecyclerAdapter
import {pkg}.databinding.FragmentHomeBinding
import {pkg}.model.ItemModel

class HomeFragment : Fragment() {{
    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {{
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        
        val items = listOf(
            ItemModel("Item 1", "Description 1"),
            ItemModel("Item 2", "Description 2"),
            ItemModel("Item 3", "Description 3"),
            ItemModel("Item 4", "Description 4")
        )

        binding.recyclerView.setHasFixedSize(true)
        binding.recyclerView.layoutManager = LinearLayoutManager(requireContext())
        binding.recyclerView.adapter = RecyclerAdapter(items) {{ selectedItem ->
            val intent = Intent(requireContext(), SecondActivity::class.java)
            intent.putExtra("EXTRA_TITLE", selectedItem.title)
            startActivity(intent)
        }}
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{base}/ui/HomeFragment.kt", home_fragment)

pager_fragment = f"""package {pkg}.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import {pkg}.adapter.ViewPagerAdapter
import {pkg}.databinding.FragmentPagerBinding

class ShowcasePagerFragment : Fragment() {{
    private var _binding: FragmentPagerBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {{
        _binding = FragmentPagerBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        val pages = listOf("Slide 1", "Slide 2", "Slide 3")
        binding.viewPager.adapter = ViewPagerAdapter(pages)
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{base}/ui/ShowcasePagerFragment.kt", pager_fragment)

form_fragment = f"""package {pkg}.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.google.android.material.dialog.MaterialAlertDialogBuilder
import {pkg}.databinding.FragmentFormBinding

class FormFragment : Fragment() {{
    private var _binding: FragmentFormBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {{
        _binding = FragmentFormBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        
        val flavors = arrayOf("Vanilla", "Chocolate", "Mango", "Strawberry")
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, flavors)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        binding.spinnerFlavor.adapter = adapter
        
        binding.spinnerFlavor.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {{
            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {{
                Toast.makeText(requireContext(), "You have selected ${{flavors[position]}} flavor", Toast.LENGTH_SHORT).show()
            }}

            override fun onNothingSelected(parent: AdapterView<*>?) {{}}
        }}

        binding.btnAlert.setOnClickListener {{
            MaterialAlertDialogBuilder(requireContext())
                .setTitle("Snapchat")
                .setMessage("Are you sure you want to uninstall?")
                .setPositiveButton("Yes") {{ _, _ ->
                    Toast.makeText(requireContext(), "The app is successfully uninstalled", Toast.LENGTH_SHORT).show()
                }}
                .setNegativeButton("No") {{ dialog, _ ->
                    dialog.dismiss()
                }}
                .show()
        }}
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{base}/ui/FormFragment.kt", form_fragment)

legacy_list_fragment = f"""package {pkg}.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.fragment.app.Fragment
import {pkg}.databinding.FragmentLegacyListBinding

class LegacyListFragment : Fragment() {{
    private var _binding: FragmentLegacyListBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {{
        _binding = FragmentLegacyListBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        val items = listOf("Apple", "Banana", "Cherry", "Date", "Elderberry")
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_list_item_1, items)
        binding.listView.adapter = adapter
        
        binding.listView.setOnItemClickListener {{ _, _, position, _ ->
            Toast.makeText(requireContext(), "You have clicked on ${{items[position]}}", Toast.LENGTH_SHORT).show()
        }}
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{base}/ui/LegacyListFragment.kt", legacy_list_fragment)

print("Generation complete")
