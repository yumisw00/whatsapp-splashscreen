package com.showcase.allinone.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.showcase.allinone.databinding.ItemCardBinding
import com.showcase.allinone.model.ItemModel

class RecyclerAdapter(
    private val items: List<ItemModel>,
    private val onItemClick: (ItemModel) -> Unit
) : RecyclerView.Adapter<RecyclerAdapter.ViewHolder>() {

    inner class ViewHolder(val binding: ItemCardBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(item: ItemModel) {
            binding.tvTitle.text = item.title
            binding.tvSubtitle.text = item.subtitle
            binding.root.setOnClickListener { onItemClick(item) }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemCardBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(items[position])
    }

    override fun getItemCount() = items.size
}