package com.showcase.allinone.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.showcase.allinone.databinding.FragmentLegacyListBinding

class LegacyListFragment : Fragment() {
    private var _binding: FragmentLegacyListBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        _binding = FragmentLegacyListBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val items = listOf("Apple", "Banana", "Cherry", "Date", "Elderberry")
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_list_item_1, items)
        binding.listView.adapter = adapter
        
        binding.listView.setOnItemClickListener { _, _, position, _ ->
            Toast.makeText(requireContext(), "You have clicked on ${items[position]}", Toast.LENGTH_SHORT).show()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}