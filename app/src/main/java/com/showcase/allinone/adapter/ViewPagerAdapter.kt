package com.showcase.allinone.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.showcase.allinone.databinding.PageLayoutBinding

class ViewPagerAdapter(private val pages: List<String>) : RecyclerView.Adapter<ViewPagerAdapter.PagerViewHolder>() {

    inner class PagerViewHolder(val binding: PageLayoutBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(text: String) {
            binding.tvPage.text = text
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PagerViewHolder {
        val binding = PageLayoutBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return PagerViewHolder(binding)
    }

    override fun onBindViewHolder(holder: PagerViewHolder, position: Int) {
        holder.bind(pages[position])
    }

    override fun getItemCount() = pages.size
}