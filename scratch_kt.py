import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

pkg_path = "app/src/main/java/com/whatsapp/splashscreen"
pkg = "com.whatsapp.splashscreen"

main_activity_kt = f"""package {pkg}

import android.os.Bundle
import android.view.MenuItem
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import androidx.fragment.app.Fragment
import {pkg}.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {{

    private lateinit var binding: ActivityMainBinding
    private lateinit var toggle: ActionBarDrawerToggle

    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.toolbar)

        toggle = ActionBarDrawerToggle(
            this, binding.drawerLayout, binding.toolbar,
            R.string.open_drawer, R.string.close_drawer
        )
        binding.drawerLayout.addDrawerListener(toggle)
        toggle.syncState()

        binding.bottomNav.setOnItemSelectedListener {{ item ->
            when (item.itemId) {{
                R.id.nav_home -> replaceFragment(HomeFragment())
                R.id.nav_showcase -> replaceFragment(ShowcaseFragment())
                R.id.nav_form -> replaceFragment(FormFragment())
                R.id.nav_legacy -> replaceFragment(LegacyListFragment())
            }}
            true
        }}

        binding.navView.setNavigationItemSelectedListener {{ item ->
            when (item.itemId) {{
                R.id.nav_home -> binding.bottomNav.selectedItemId = R.id.nav_home
                R.id.nav_showcase -> binding.bottomNav.selectedItemId = R.id.nav_showcase
                R.id.nav_form -> binding.bottomNav.selectedItemId = R.id.nav_form
                R.id.nav_legacy -> binding.bottomNav.selectedItemId = R.id.nav_legacy
            }}
            binding.drawerLayout.closeDrawer(GravityCompat.START)
            true
        }}

        if (savedInstanceState == null) {{
            binding.bottomNav.selectedItemId = R.id.nav_home
        }}
    }}

    private fun replaceFragment(fragment: Fragment) {{
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragment_container, fragment)
            .commit()
    }}
}}
"""
write_file(f"{pkg_path}/MainActivity.kt", main_activity_kt)

home_fragment_kt = f"""package {pkg}

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import {pkg}.databinding.FragmentHomeBinding

class HomeFragment : Fragment() {{
    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {{
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        val data = listOf(
            ItemData("Item 1", "Subtitle 1"),
            ItemData("Item 2", "Subtitle 2"),
            ItemData("Item 3", "Subtitle 3"),
            ItemData("Item 4", "Subtitle 4"),
            ItemData("Item 5", "Subtitle 5")
        )
        binding.recyclerView.layoutManager = LinearLayoutManager(requireContext())
        binding.recyclerView.adapter = ItemAdapter(data)
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{pkg_path}/HomeFragment.kt", home_fragment_kt)

item_data_kt = f"""package {pkg}

data class ItemData(val title: String, val subtitle: String)
"""
write_file(f"{pkg_path}/ItemData.kt", item_data_kt)

item_adapter_kt = f"""package {pkg}

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import {pkg}.databinding.ItemLayoutBinding

class ItemAdapter(private val items: List<ItemData>) : RecyclerView.Adapter<ItemAdapter.ItemViewHolder>() {{

    inner class ItemViewHolder(private val binding: ItemLayoutBinding) : RecyclerView.ViewHolder(binding.root) {{
        fun bind(item: ItemData) {{
            binding.tvTitle.text = item.title
            binding.tvSubtitle.text = item.subtitle
        }}
    }}

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {{
        val binding = ItemLayoutBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ItemViewHolder(binding)
    }}

    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {{
        holder.bind(items[position])
    }}

    override fun getItemCount() = items.size
}}
"""
write_file(f"{pkg_path}/ItemAdapter.kt", item_adapter_kt)

showcase_fragment_kt = f"""package {pkg}

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import {pkg}.databinding.FragmentShowcaseBinding

class ShowcaseFragment : Fragment() {{
    private var _binding: FragmentShowcaseBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {{
        _binding = FragmentShowcaseBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        val pages = listOf("Page 1", "Page 2", "Page 3")
        binding.viewPager.adapter = ShowcasePagerAdapter(this, pages)
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{pkg_path}/ShowcaseFragment.kt", showcase_fragment_kt)

showcase_pager_adapter_kt = f"""package {pkg}

import android.os.Bundle
import androidx.fragment.app.Fragment
import androidx.viewpager2.adapter.FragmentStateAdapter

class ShowcasePagerAdapter(fragment: Fragment, private val pages: List<String>) : FragmentStateAdapter(fragment) {{
    override fun getItemCount(): Int = pages.size

    override fun createFragment(position: Int): Fragment {{
        val fragment = ShowcasePageFragment()
        fragment.arguments = Bundle().apply {{
            putString("content", pages[position])
        }}
        return fragment
    }}
}}
"""
write_file(f"{pkg_path}/ShowcasePagerAdapter.kt", showcase_pager_adapter_kt)

showcase_page_fragment_kt = f"""package {pkg}

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import {pkg}.databinding.FragmentShowcasePageBinding

class ShowcasePageFragment : Fragment() {{
    private var _binding: FragmentShowcasePageBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {{
        _binding = FragmentShowcasePageBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        binding.tvPageContent.text = arguments?.getString("content") ?: "Unknown"
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{pkg_path}/ShowcasePageFragment.kt", showcase_page_fragment_kt)

form_fragment_kt = f"""package {pkg}

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.Fragment
import {pkg}.databinding.FragmentFormBinding

class FormFragment : Fragment() {{
    private var _binding: FragmentFormBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {{
        _binding = FragmentFormBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        
        val options = arrayOf("Option A", "Option B", "Option C")
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, options)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        binding.spinnerOptions.adapter = adapter
        
        binding.spinnerOptions.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {{
            override fun onItemSelected(parent: AdapterView<*>, view: View?, position: Int, id: Long) {{
                Toast.makeText(context, "Selected: ${{options[position]}}", Toast.LENGTH_SHORT).show()
            }}

            override fun onNothingSelected(parent: AdapterView<*>) {{}}
        }}

        binding.btnShowDialog.setOnClickListener {{
            AlertDialog.Builder(requireContext())
                .setTitle("Dialog Title")
                .setMessage("This is a simple alert dialog.")
                .setPositiveButton("OK") {{ dialog, _ ->
                    dialog.dismiss()
                }}
                .show()
        }}
        
        binding.btnOpenDetail.setOnClickListener {{
            val intent = Intent(requireContext(), DetailActivity::class.java)
            startActivity(intent)
        }}
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{pkg_path}/FormFragment.kt", form_fragment_kt)

legacy_list_fragment_kt = f"""package {pkg}

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import {pkg}.databinding.FragmentLegacyListBinding

class LegacyListFragment : Fragment() {{
    private var _binding: FragmentLegacyListBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {{
        _binding = FragmentLegacyListBinding.inflate(inflater, container, false)
        return binding.root
    }}

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {{
        super.onViewCreated(view, savedInstanceState)
        val items = listOf("Legacy Item 1", "Legacy Item 2", "Legacy Item 3", "Legacy Item 4")
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_list_item_1, items)
        binding.listView.adapter = adapter
    }}

    override fun onDestroyView() {{
        super.onDestroyView()
        _binding = null
    }}
}}
"""
write_file(f"{pkg_path}/LegacyListFragment.kt", legacy_list_fragment_kt)

detail_activity_kt = f"""package {pkg}

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import {pkg}.databinding.ActivityDetailBinding

class DetailActivity : AppCompatActivity() {{

    private lateinit var binding: ActivityDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        binding = ActivityDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnOpenBrowser.setOnClickListener {{
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.google.com"))
            startActivity(intent)
        }}
    }}
}}
"""
write_file(f"{pkg_path}/DetailActivity.kt", detail_activity_kt)
