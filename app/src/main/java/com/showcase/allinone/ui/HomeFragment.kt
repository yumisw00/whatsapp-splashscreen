package com.showcase.allinone.ui

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.showcase.allinone.SecondActivity
import com.showcase.allinone.adapter.RecyclerAdapter
import com.showcase.allinone.databinding.FragmentHomeBinding
import com.showcase.allinone.model.ItemModel

class HomeFragment : Fragment() {
    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        val items = listOf(
            ItemModel("Item 1", "Description 1"),
            ItemModel("Item 2", "Description 2"),
            ItemModel("Item 3", "Description 3"),
            ItemModel("Item 4", "Description 4")
        )

        binding.recyclerView.setHasFixedSize(true)
        binding.recyclerView.layoutManager = LinearLayoutManager(requireContext())
        binding.recyclerView.adapter = RecyclerAdapter(items) { selectedItem ->
            val intent = Intent(requireContext(), SecondActivity::class.java)
            intent.putExtra("EXTRA_TITLE", selectedItem.title)
            startActivity(intent)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}