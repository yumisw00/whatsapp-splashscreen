package com.showcase.allinone.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.google.android.material.dialog.MaterialAlertDialogBuilder
import com.showcase.allinone.databinding.FragmentFormBinding

class FormFragment : Fragment() {
    private var _binding: FragmentFormBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        _binding = FragmentFormBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        val flavors = arrayOf("Vanilla", "Chocolate", "Mango", "Strawberry")
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, flavors)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        binding.spinnerFlavor.adapter = adapter
        
        binding.spinnerFlavor.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                Toast.makeText(requireContext(), "You have selected ${flavors[position]} flavor", Toast.LENGTH_SHORT).show()
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {}
        }

        binding.btnAlert.setOnClickListener {
            MaterialAlertDialogBuilder(requireContext())
                .setTitle("Snapchat")
                .setMessage("Are you sure you want to uninstall?")
                .setPositiveButton("Yes") { _, _ ->
                    Toast.makeText(requireContext(), "The app is successfully uninstalled", Toast.LENGTH_SHORT).show()
                }
                .setNegativeButton("No") { dialog, _ ->
                    dialog.dismiss()
                }
                .show()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}