package com.showcase.allinone

import android.os.Bundle
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.core.view.GravityCompat
import androidx.fragment.app.Fragment
import com.showcase.allinone.databinding.ActivityMainBinding
import com.showcase.allinone.ui.FormFragment
import com.showcase.allinone.ui.HomeFragment
import com.showcase.allinone.ui.LegacyListFragment
import com.showcase.allinone.ui.ShowcasePagerFragment

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var toggle: ActionBarDrawerToggle

    override fun onCreate(savedInstanceState: Bundle?) {
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

        binding.navView.setNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_home -> binding.bottomNav.selectedItemId = R.id.bottom_home
                R.id.nav_settings -> Toast.makeText(this, "Settings clicked", Toast.LENGTH_SHORT).show()
                R.id.nav_share -> Toast.makeText(this, "Share clicked", Toast.LENGTH_SHORT).show()
                R.id.nav_about -> Toast.makeText(this, "About clicked", Toast.LENGTH_SHORT).show()
                R.id.nav_logout -> Toast.makeText(this, "Logout clicked", Toast.LENGTH_SHORT).show()
            }
            binding.drawerLayout.closeDrawer(GravityCompat.START)
            true
        }

        binding.bottomNav.setOnItemSelectedListener { item ->
            when (item.itemId) {
                R.id.bottom_home -> replaceFragment(HomeFragment())
                R.id.bottom_search -> replaceFragment(ShowcasePagerFragment())
                R.id.bottom_add -> {
                    Toast.makeText(this, "upload image and video", Toast.LENGTH_SHORT).show()
                    return@setOnItemSelectedListener false
                }
                R.id.bottom_reels -> replaceFragment(FormFragment())
                R.id.bottom_profile -> replaceFragment(LegacyListFragment())
            }
            true
        }

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (binding.drawerLayout.isDrawerOpen(GravityCompat.START)) {
                    binding.drawerLayout.closeDrawer(GravityCompat.START)
                } else {
                    isEnabled = false
                    onBackPressedDispatcher.onBackPressed()
                }
            }
        })

        if (savedInstanceState == null) {
            binding.bottomNav.selectedItemId = R.id.bottom_home
        }
    }

    private fun replaceFragment(fragment: Fragment) {
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragment_container, fragment)
            .commit()
    }
}