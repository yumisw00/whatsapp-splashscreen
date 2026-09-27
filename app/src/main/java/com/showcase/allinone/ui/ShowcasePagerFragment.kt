package com.showcase.allinone.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.showcase.allinone.adapter.ViewPagerAdapter
import com.showcase.allinone.databinding.FragmentPagerBinding

class ShowcasePagerFragment : Fragment() {
    private var _binding: FragmentPagerBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        _binding = FragmentPagerBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val pages = listOf("Slide 1", "Slide 2", "Slide 3")
        binding.viewPager.adapter = ViewPagerAdapter(pages)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}